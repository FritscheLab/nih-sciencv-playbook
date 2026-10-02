// Some diagram types in Mermaid 11.17.2 need metadata supplied after rendering.
// Use commented accTitle/accDescr for types whose grammar rejects directives.
export function enhanceDiagram(element, source) {
  const svg = element.querySelector('svg');
  const container = element.closest('pre');
  if (!svg || !container) return;

  for (const [tag, directive, attribute] of [
    ['title', 'accTitle', 'aria-labelledby'],
    ['desc', 'accDescr', 'aria-describedby'],
  ]) {
    let metadata = svg.querySelector(`:scope > ${tag}`);
    const value = source.match(new RegExp(`^\\s*(?:%%\\s*)?${directive}:\\s*(.+)$`, 'm'))?.[1];
    if (!metadata && value) {
      metadata = document.createElementNS('http://www.w3.org/2000/svg', tag);
      metadata.textContent = value.trim();
      svg.prepend(metadata);
    }
    if (metadata) {
      if (!metadata.id) metadata.id = `${svg.id}-${tag}`;
      svg.setAttribute(attribute, metadata.id);
    }
  }
  svg.setAttribute('role', 'img');

  // Preserve the renderer's font sizes instead of scaling the SVG to the column.
  if (svg.viewBox.baseVal.width > 0) {
    svg.style.width = `${svg.viewBox.baseVal.width}px`;
    svg.style.maxWidth = 'none';
  }

  const figure = document.createElement('figure');
  figure.className = 'mermaid-figure';
  container.before(figure);
  figure.append(container);
  container.classList.add('mermaid-scroll');
  const hint = document.createElement('figcaption');
  hint.className = 'mermaid-scroll-hint';
  hint.id = `${svg.id}-scroll-hint`;
  hint.textContent = 'Scroll sideways to view the full diagram. With a keyboard, focus the diagram and use the left and right arrow keys.';
  figure.append(hint);

  const title = svg.querySelector(':scope > title')?.textContent || 'Diagram';
  function updateScrolling() {
    const scrollable = container.scrollWidth > container.clientWidth + 1;
    hint.hidden = !scrollable;
    container.classList.toggle('is-scrollable', scrollable);
    if (scrollable) {
      container.tabIndex = 0;
      container.setAttribute('role', 'region');
      container.setAttribute('aria-label', `${title} - scrollable diagram`);
      container.setAttribute('aria-describedby', hint.id);
    } else {
      for (const attribute of ['tabindex', 'role', 'aria-label', 'aria-describedby']) {
        container.removeAttribute(attribute);
      }
    }
  }
  updateScrolling();
  new ResizeObserver(updateScrolling).observe(container);

  // Show the entry label initially, even when the diagram is asymmetric.
  const labels = [...svg.querySelectorAll('.nodeLabel')].filter(label => label.textContent.trim());
  let entry;
  if (/^\s*mindmap/.test(source)) entry = svg.querySelector('.section-root .nodeLabel');
  else if (/^\s*(flowchart|stateDiagram)/.test(source)) {
    entry = labels.sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)[0];
  } else if (/^\s*block-beta/.test(source)) entry = labels[0];
  if (entry) {
    const label = entry.getBoundingClientRect();
    const viewport = container.getBoundingClientRect();
    container.scrollLeft = Math.max(0, label.x + label.width / 2 - viewport.x - container.clientWidth / 2);
  }
  element.dataset.mermaidEnhanced = 'true';
}
