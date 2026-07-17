from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
out_path = str(REPO_ROOT / "docs" / "assets" / "SciENcv_XML_Accelerator_GenAI_Cheat_Sheet_v2_3pages.pdf")
Path(out_path).parent.mkdir(parents=True, exist_ok=True)

# ----- Styles -----
styles = getSampleStyleSheet()

COLOR_PRIMARY = colors.HexColor("#0B3D91")
COLOR_MUTED = colors.HexColor("#555555")
COLOR_LINE = colors.HexColor("#C7D2E8")
COLOR_CALLOUT_BG = colors.HexColor("#F6F9FF")
COLOR_WARN_BG = colors.HexColor("#FFF8E6")

styles.add(ParagraphStyle(name="H1", fontSize=20, leading=24, alignment=1, textColor=COLOR_PRIMARY, spaceAfter=10))
styles.add(ParagraphStyle(name="Subtitle", fontSize=11, leading=14, alignment=1, textColor=COLOR_MUTED, spaceAfter=16))
styles.add(ParagraphStyle(name="H2", fontSize=14, leading=18, textColor=COLOR_PRIMARY, spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name="H3", fontSize=11.5, leading=15, textColor=COLOR_PRIMARY, spaceBefore=6, spaceAfter=6))
styles.add(ParagraphStyle(name="Body", fontSize=10.5, leading=14, textColor=colors.black, spaceAfter=7))
styles.add(ParagraphStyle(name="BodyMuted", fontSize=10.2, leading=13.5, textColor=COLOR_MUTED, spaceAfter=7))
styles.add(ParagraphStyle(name="Small", fontSize=9.2, leading=12.2, textColor=COLOR_MUTED, spaceAfter=6))
styles.add(ParagraphStyle(name="Tag", fontSize=9.2, leading=12, textColor=COLOR_PRIMARY))
styles.add(ParagraphStyle(name="TblHead", fontSize=9.8, leading=12.6, textColor=colors.black, spaceAfter=0))
styles.add(ParagraphStyle(name="TblCell", fontSize=9.4, leading=12.2, textColor=colors.black, spaceAfter=0))

# Header/Footer
def on_page(canvas, doc):
    canvas.saveState()
    w, h = LETTER
    canvas.setStrokeColor(COLOR_LINE)
    canvas.setLineWidth(1)
    canvas.line(doc.leftMargin, h - 0.62*inch, w - doc.rightMargin, h - 0.62*inch)

    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(COLOR_PRIMARY)
    canvas.drawString(doc.leftMargin, h - 0.50*inch, "SciENcv XML Accelerator: GenAI Cheat Sheet")

    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(COLOR_MUTED)
    canvas.drawRightString(w - doc.rightMargin, 0.50*inch, f"Page {doc.page}")
    canvas.restoreState()

doc = BaseDocTemplate(
    out_path,
    pagesize=LETTER,
    leftMargin=0.78*inch,
    rightMargin=0.78*inch,
    topMargin=0.92*inch,
    bottomMargin=0.78*inch,
)

frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 0.20*inch, id="normal")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=on_page)])

story = []

# ==================== PAGE 1 ====================
story.append(Paragraph("SciENcv XML Accelerator: GenAI Cheat Sheet", styles["H1"]))
story.append(Paragraph("A practical, print-friendly quick reference for generating NIH CPOS (Other Support) XML with GenAI.", styles["Subtitle"]))

story.append(Paragraph("Quick Start Workflow (End-to-end)", styles["H2"]))
flow = Table(
    [[
        Paragraph("<b>1) Choose model</b><br/><font color='#555555'>Use a high-reasoning mode</font>", styles["Body"]),
        Paragraph("<b>2) Prepare inputs</b><br/><font color='#555555'>Other Support + changes</font>", styles["Body"]),
        Paragraph("<b>3) Run prompt</b><br/><font color='#555555'>Prompt + docs together</font>", styles["Body"]),
        Paragraph("<b>4) Save as .xml</b><br/><font color='#555555'>Copy code only</font>", styles["Body"]),
    ],
     [
        Paragraph("<b>5) Validate + format</b><br/><font color='#555555'>Check structure + limits</font>", styles["Body"]),
        Paragraph("<b>6) Upload + review</b><br/><font color='#555555'>Fix missing fields</font>", styles["Body"]),
        Paragraph("<b>7) Final human check</b><br/><font color='#555555'>Line-by-line</font>", styles["Body"]),
        Paragraph("<b>8) Save XML snapshot + final PDF</b><br/><font color='#555555'>XML may diverge after SciENcv edits</font>", styles["Body"]),
     ]],
    colWidths=[doc.width/4.0]*4
)
flow.setStyle(TableStyle([
    ("BOX", (0,0), (-1,-1), 1, COLOR_LINE),
    ("INNERGRID", (0,0), (-1,-1), 0.7, COLOR_LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
]))
story.append(flow)
story.append(Spacer(1, 10))

story.append(Paragraph("1) Select the Right Model (Critical)", styles["H2"]))
story.append(Paragraph(
    "Avoid \"Auto\" or speed-optimized modes. For XML generation, you want a model that plans structure and validates details.",
    styles["BodyMuted"]
))

# Model selection table with proper wrapping
model_rows = [
    [
        Paragraph("<b>Platform</b>", styles["TblHead"]),
        Paragraph("<b>Avoid</b>", styles["TblHead"]),
        Paragraph("<b>Select</b>", styles["TblHead"]),
        Paragraph("<b>Why it matters</b>", styles["TblHead"]),
    ],
    [
        Paragraph("Google", styles["TblCell"]),
        Paragraph("Gemini Flash / Auto", styles["TblCell"]),
        Paragraph("<b>Gemini 3 Pro</b>", styles["TblCell"]),
        Paragraph("Better adherence to structured prompts; fewer broken tags.", styles["TblCell"]),
    ],
    [
        Paragraph("Microsoft Copilot", styles["TblCell"]),
        Paragraph("Balanced / Creative", styles["TblCell"]),
        Paragraph("<b>Think Deeper / Reasoning</b>", styles["TblCell"]),
        Paragraph("Reduces date/format mistakes and improves consistency.", styles["TblCell"]),
    ],
    [
        Paragraph("OpenAI", styles["TblCell"]),
        Paragraph("Speed / default", styles["TblCell"]),
        Paragraph("<b>Reasoning mode</b>", styles["TblCell"]),
        Paragraph("Plans XML hierarchy before emitting code; fewer invalid fields.", styles["TblCell"]),
    ],
]

col1, col2, col3 = 1.2*inch, 1.55*inch, 1.55*inch
model_tbl = Table(model_rows, colWidths=[col1, col2, col3, doc.width - (col1+col2+col3)])
model_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#E9EFFA")),
    ("TEXTCOLOR", (0,0), (-1,0), COLOR_PRIMARY),
    ("GRID", (0,0), (-1,-1), 0.6, COLOR_LINE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(model_tbl)
story.append(Spacer(1, 10))

callout = Table(
    [[Paragraph("<b>Rule of thumb</b>", styles["Tag"]),
      Paragraph("If the model responds instantly, you are likely in the wrong mode. High-quality XML often takes 10-30 seconds of reasoning.", styles["Small"]) ]],
    colWidths=[1.25*inch, doc.width - 1.25*inch]
)
callout.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), COLOR_CALLOUT_BG),
    ("BOX", (0,0), (-1,-1), 1, COLOR_LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
]))
story.append(callout)

# ==================== PAGE 2 ====================
story.append(PageBreak())

story.append(Paragraph("2) Inputs and Prompting: Get Clean Source Data", styles["H2"]))
story.append(Paragraph(
    "Your output quality is capped by your input quality. Use the simplest, cleanest source that reflects the current state of support.",
    styles["BodyMuted"]
))

story.append(Paragraph("Choose an input method", styles["H3"]))
inputs_list = ListFlowable(
    [
        ListItem(Paragraph("<b>Option A: Copy/paste text (highest accuracy)</b><br/>Open the source document, select all, copy, and paste into the prompt. This strips hidden formatting and reduces table-read errors.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Option B: Attach files (best for long docs)</b><br/>Attach PDF/Word/Excel files. If tables are complex, add: <i>Read tables row-by-row carefully.</i>", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Best practice from the workflow</b><br/>If you have a prior Other Support plus updates, provide both the source and a short \"changes\" note in the same run so the model has one coherent instruction set.", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet",
    leftIndent=18,
    bulletFontName="Helvetica",
    bulletFontSize=10
)
story.append(inputs_list)
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_LINE, spaceBefore=6, spaceAfter=10))

story.append(Paragraph("3) Output Handling: Turn Model Output Into a Valid XML File", styles["H2"]))
warn = Table(
    [[Paragraph("<b>Critical:</b> SciENcv needs a real <u>plain-text</u> XML file. Do not upload a chat transcript or formatted AI response.", styles["Body"]) ]],
    colWidths=[doc.width]
)
warn.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), COLOR_WARN_BG),
    ("BOX", (0,0), (-1,-1), 1, colors.HexColor("#E0C36B")),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(warn)
story.append(Spacer(1, 8))

story.append(Paragraph("Do this every time:", styles["H3"]))
save_steps = ListFlowable(
    [
        ListItem(Paragraph("<b>Copy only the XML code block</b> (use the UI's <i>Copy code</i> button). Do not copy surrounding explanation text.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Paste into a plain-text editor</b>: Notepad (Windows) or TextEdit in plain-text mode (macOS).", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Save as an XML file</b>:", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Windows Notepad: <i>File -> Save As</i> -> <b>Save as type: All Files</b> -> filename ends with <b>.xml</b> (example: <span face='Courier'>OtherSupport.xml</span>).", styles["Body"]), leftIndent=28),
        ListItem(Paragraph("macOS TextEdit: <i>Format -> Make Plain Text</i> -> Save -> ensure the filename ends with <b>.xml</b>.", styles["Body"]), leftIndent=28),
        ListItem(Paragraph("<b>Expected behavior:</b> your computer may show the file as a \"webpage\" or \"HTML document\" - that is normal. What matters is that it is plain text and ends in <b>.xml</b>.", styles["Body"]), leftIndent=12),
    ],
    bulletType="1",
    start="1",
    leftIndent=18,
    bulletFontName="Helvetica",
    bulletFontSize=10
)
story.append(save_steps)

story.append(Spacer(1, 8))
story.append(Paragraph("Quick sanity checks (before validation):", styles["H3"]))
sanity = ListFlowable(
    [
        ListItem(Paragraph("File opens as readable text and starts with &lt;?xml or an opening XML tag.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Use straight ASCII quotes as XML attribute delimiters; Unicode punctuation is valid in element text.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Dates are consistent and complete (month/day/year where required).", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(sanity)

# ==================== PAGE 3 ====================
story.append(PageBreak())

story.append(Paragraph("4) Validate, Upload, and Review (Mandatory)", styles["H2"]))
story.append(Paragraph(
    "Treat validation as a required gate before upload. The validator catches malformed XML, structural errors, invalid field values, and length-limit violations.",
    styles["BodyMuted"]
))

story.append(Paragraph("Browser XML Validator", styles["H3"]))
story.append(Paragraph("Validator URL: https://fritschelab.github.io/nih-sciencv-playbook/other-support/xml-upload/validator.html", styles["Small"]))

validator_steps = ListFlowable(
    [
        ListItem(Paragraph("<b>Paste</b> the XML into the validator.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Run <b>Validate</b> and address reported errors; valid Unicode punctuation can remain unchanged.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Run <b>Format XML</b> (makes debugging easier).", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("If you see a red error (example: <i>Line 45: Invalid Date</i>), paste the error back to the model and ask it to fix only that issue.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Save</b> the validated XML and use that file for upload.", styles["Body"]), leftIndent=12),
    ],
    bulletType="1", start="1", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(validator_steps)

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_LINE, spaceBefore=6, spaceAfter=10))

story.append(Paragraph("Upload to MyNCBI / SciENcv and complete required fields", styles["H3"]))
upload_notes = ListFlowable(
    [
        ListItem(Paragraph("Upload the cleaned XML into SciENcv CPOS import.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("SciENcv may flag missing or incomplete fields (common: objectives, effort, dates). Fill or correct these in the SciENcv interface.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Some requirements are outside the XML (for example ORCID linkage and profile setup). Those must be completed in MyNCBI/SciENcv/ORCID by the PI.", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(upload_notes)

story.append(Spacer(1, 10))
story.append(Paragraph("Human review is non-negotiable", styles["H3"]))
review_box = Table(
    [[Paragraph(
        "<b>Quality control checklist</b><br/>"
        "1) Compare every imported entry line-by-line against the source Other Support document.<br/>"
        "2) Confirm totals, effort values, and dates (especially consultant roles).<br/>"
        "3) Watch for format differences across sources (for example VA vs university formats).",
        styles["Body"]
    )]],
    colWidths=[doc.width]
)
review_box.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), COLOR_CALLOUT_BG),
    ("BOX", (0,0), (-1,-1), 1, COLOR_LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(review_box)

story.append(Spacer(1, 10))
story.append(Paragraph("Future updates", styles["H3"]))
story.append(Paragraph(
    "Save the cleaned, validated XML you uploaded as an intermediate snapshot (useful for regeneration and troubleshooting). Note: after you make manual edits in SciENcv, the uploaded XML may no longer match the current record. For future revisions, also save the final exported Other Support PDF (and, if possible, a brief note of any manual edits) so your next update starts from the most current content.",
    styles["Body"]
))

story.append(Spacer(1, 8))
story.append(Paragraph("Notes", styles["H3"]))
story.append(Paragraph(
    "The playbook is a public resource and includes disclaimers that it is not official NIH guidance. GenAI accelerates drafting but does not replace expert review.",
    styles["BodyMuted"]
))

doc.build(story)

out_path
