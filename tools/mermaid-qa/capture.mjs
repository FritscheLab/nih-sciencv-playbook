import fs from 'node:fs/promises';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import puppeteer from 'puppeteer-core';

const { values } = parseArgs({ options: {
  site: { type: 'string' }, output: { type: 'string' }, browser: { type: 'string' },
} });
if (!values.site || !values.output || !values.browser) {
  throw new Error('Required arguments: --site BUILT_SITE --output QA_DIRECTORY --browser CHROME_PATH');
}
const repo = fileURLToPath(new URL('../../', import.meta.url));
const site = await fs.realpath(values.site);
const output = path.resolve(values.output);
const runtime = fileURLToPath(new URL('node_modules/mermaid/dist/', import.meta.url));
const config = await fs.readFile(path.join(repo, 'docs/_config.yml'), 'utf8');
const version = config.match(/^mermaid:\s*\n\s+version:\s*["']?([\d.]+)/m)?.[1];
const baseurl = config.match(/^baseurl:\s*["']?([^"'\s]*)/m)?.[1] || '';
const installed = JSON.parse(await fs.readFile(new URL('node_modules/mermaid/package.json', import.meta.url), 'utf8'));
if (!version || version !== installed.version) {
  throw new Error(`Mermaid version mismatch: site=${version}, installed=${installed.version}`);
}
if (output === site || output.startsWith(site + path.sep) || output === path.join(repo, 'docs') || output.startsWith(path.join(repo, 'docs') + path.sep)) {
  throw new Error('Keep QA output outside the built or published site.');
}

async function markdownFiles(directory) {
  const files = [];
  for (const item of await fs.readdir(directory, { withFileTypes: true })) {
    const target = path.join(directory, item.name);
    if (item.isDirectory() && !item.name.startsWith('.') && item.name !== '_site') {
      files.push(...await markdownFiles(target));
    } else if (item.isFile() && item.name.endsWith('.md')) files.push(target);
  }
  return files.sort();
}
const inventory = [];
for (const file of await markdownFiles(path.join(repo, 'docs'))) {
  const source = await fs.readFile(file, 'utf8');
  let ordinal = 0;
  for (const match of source.matchAll(/^```mermaid\s*\n([\s\S]*?)^```\s*$/gm)) {
    inventory.push({
      path: path.relative(repo, file), line: source.slice(0, match.index).split('\n').length,
      ordinal: ++ordinal, type: match[1].trim().split('\n')[0], source: match[1],
    });
  }
}
if (!inventory.length) throw new Error('No Mermaid diagrams found.');
await fs.mkdir(path.join(output, 'screenshots'), { recursive: true });
await fs.writeFile(path.join(output, 'inventory.json'), JSON.stringify(inventory, null, 2));

const mime = { '.html': 'text/html', '.js': 'application/javascript', '.mjs': 'application/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.json': 'application/json' };
const server = http.createServer(async (request, response) => {
  try {
    let route = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    if (baseurl && route.startsWith(baseurl + '/')) route = route.slice(baseurl.length);
    if (route.endsWith('/')) route += 'index.html';
    const file = path.resolve(site, '.' + route);
    if (!file.startsWith(site + path.sep)) throw new Error('Invalid path');
    const body = await fs.readFile(file);
    response.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' });
    response.end(body);
  } catch { response.writeHead(404); response.end('Not found'); }
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const port = server.address().port;
let browser;
const report = { capturedAt: new Date().toISOString(), mermaid: version, viewports: [1440, 390], pages: [] };
try {
  browser = await puppeteer.launch({ executablePath: values.browser, headless: true });
  report.browser = await browser.version();
  console.log(`${report.browser}; Mermaid ${version}; ${inventory.length} diagrams`);
  for (const width of report.viewports) {
    const page = await browser.newPage();
    await page.setViewport({ width, height: 1000, deviceScaleFactor: 1 });
    await page.setRequestInterception(true);
    let errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', async request => {
      const prefix = `https://cdn.jsdelivr.net/npm/mermaid@${version}/dist/`;
      if (request.url().startsWith('https://cdn.jsdelivr.net/npm/mermaid@') && !request.url().startsWith(prefix)) {
        errors.push(`Unexpected Mermaid runtime: ${request.url()}`);
        await request.abort(); return;
      }
      if (!request.url().startsWith(prefix)) { await request.continue(); return; }
      try {
        const relative = decodeURIComponent(request.url().slice(prefix.length).split('?')[0]);
        const file = path.resolve(runtime, relative);
        if (!file.startsWith(runtime)) throw new Error('Invalid module path');
        await request.respond({ status: 200, contentType: 'application/javascript',
          headers: { 'Access-Control-Allow-Origin': '*' }, body: await fs.readFile(file) });
      } catch (error) { errors.push(`Mermaid module: ${error.message}`); await request.abort(); }
    });
    for (const sourcePath of new Set(inventory.map(item => item.path))) {
      errors = [];
      const route = sourcePath.replace(/^docs\//, '').replace(/\.md$/, '.html');
      const entries = inventory.filter(item => item.path === sourcePath);
      const slug = route.replace(/\.html$/, '').replaceAll('/', '--');
      const response = await page.goto(`http://127.0.0.1:${port}${baseurl}/${route}`, { waitUntil: 'networkidle0', timeout: 30000 });
      if (!response.ok()) throw new Error(`${sourcePath}: HTTP ${response.status()}`);
      if (!(await response.text()).includes(`https://cdn.jsdelivr.net/npm/mermaid@${version}/dist/mermaid.esm.min.mjs`)) {
        throw new Error(`${sourcePath}: built page does not load the pinned Mermaid runtime; rebuild the site.`);
      }
      await page.evaluate(() => document.fonts.ready);
      await page.waitForFunction(count => {
        const diagrams = [...document.querySelectorAll('.language-mermaid')];
        return diagrams.length === count && diagrams.every(element => element.dataset.mermaidEnhanced === 'true' && element.querySelector('svg'));
      }, { timeout: 10000 }, entries.length).catch(error => errors.push(error.message));
      const metrics = await page.evaluate(() => {
        const bounds = node => {
          const r = node.getBoundingClientRect();
          return { x: r.x, y: r.y, width: r.width, height: r.height };
        };
        return {
          pageWidth: document.documentElement.scrollWidth,
          content: bounds(document.querySelector('.main-content')),
          diagrams: [...document.querySelectorAll('.language-mermaid')].map((element, index) => {
            const svg = element.querySelector('svg');
            const container = element.closest('.mermaid-scroll') || element;
            if (!svg) return { ordinal: index + 1, missingSVG: true };
            const viewBox = svg.viewBox.baseVal;
            const displayed = bounds(svg);
            const scale = viewBox.width ? displayed.width / viewBox.width : 1;
            const labels = [...svg.querySelectorAll('text, foreignObject .nodeLabel, foreignObject .edgeLabel')]
              .filter(node => node.textContent.trim()).map(node => ({
                text: node.textContent.trim(), box: bounds(node),
                effectiveFont: parseFloat(getComputedStyle(node).fontSize) * scale,
              }));
            return {
              ordinal: index + 1, wrapper: bounds(container), displayed,
              viewBox: { x: viewBox.x, y: viewBox.y, width: viewBox.width, height: viewBox.height }, scale,
              wrapperScrollWidth: container.scrollWidth, scrollLeft: container.scrollLeft,
              scrollable: container.scrollWidth > container.clientWidth + 1,
              tabIndex: container.getAttribute('tabindex'), scrollRole: container.getAttribute('role'),
              scrollLabel: container.getAttribute('aria-label'),
              scrollHint: container.closest('figure')?.querySelector('figcaption:not([hidden])')?.textContent || '',
              minFont: Math.min(...labels.map(label => label.effectiveFont)), labels,
              title: svg.querySelector('title')?.textContent || '', description: svg.querySelector('desc')?.textContent || '',
              labelledBy: svg.getAttribute('aria-labelledby'), describedBy: svg.getAttribute('aria-describedby'), role: svg.getAttribute('role'),
              errorDiagram: !!svg.querySelector('.error-icon, .error-text'),
            };
          }),
        };
      });
      const pageImage = `screenshots/${slug}-${width}-page.png`;
      await page.screenshot({ path: path.join(output, pageImage), fullPage: true });
      const elements = await page.$$('.language-mermaid');
      for (let i = 0; i < elements.length; i++) {
        const diagramImage = `screenshots/${slug}-${width}-d${i + 1}.png`;
        const container = await elements[i].evaluateHandle(element => element.closest('.mermaid-scroll') || element);
        await container.screenshot({ path: path.join(output, diagramImage) });
        const svg = await elements[i].evaluate(element => element.querySelector('svg')?.outerHTML || '');
        await fs.writeFile(path.join(output, diagramImage.replace(/\.png$/, '.svg')), svg);
        metrics.diagrams[i].screenshot = diagramImage;
        metrics.diagrams[i].source = entries[i];
        // Capture the entire SVG separately from the intentional viewport crop.
        const saved = await container.evaluate(element => {
          const saved = { overflow: element.style.overflow, borderColor: element.style.borderColor, scrollLeft: element.scrollLeft };
          element.style.overflow = 'visible'; element.style.borderColor = 'transparent'; element.scrollLeft = 0;
          return saved;
        });
        const fullImage = diagramImage.replace(/\.png$/, '-full.png');
        const svgElement = await elements[i].$('svg');
        if (svgElement) {
          await svgElement.screenshot({ path: path.join(output, fullImage) });
          metrics.diagrams[i].fullScreenshot = fullImage;
        }
        await container.evaluate((element, saved) => {
          element.style.overflow = saved.overflow; element.style.borderColor = saved.borderColor; element.scrollLeft = saved.scrollLeft;
        }, saved);
      }
      report.pages.push({ path: sourcePath, width, errors: [...errors], screenshot: pageImage, ...metrics });
      await fs.writeFile(path.join(output, 'results.json'), JSON.stringify(report, null, 2));
      console.log(`${sourcePath}: ${width}px, ${metrics.diagrams.length} SVGs, ${errors.length} errors`);
    }
    await page.close();
  }
  if (report.pages.some(page => page.errors.length || page.diagrams.some(diagram => diagram.missingSVG || diagram.errorDiagram))) process.exitCode = 1;
} finally {
  if (browser) await browser.close();
  await new Promise(resolve => server.close(resolve));
}
