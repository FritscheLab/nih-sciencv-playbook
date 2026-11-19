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
story.append(Paragraph("Draft Current and Pending (Other) Support (CPOS) XML for upload into SciENcv.", styles["Subtitle"]))

story.append(Paragraph("Workflow", styles["H2"]))
flow = Table(
    [[
        Paragraph("<b>1) Check tool approval</b><br/><font color='#555555'>Follow your institution's policy</font>", styles["Body"]),
        Paragraph("<b>2) Prepare inputs</b><br/><font color='#555555'>Other Support + changes</font>", styles["Body"]),
        Paragraph("<b>3) Run the prompt</b><br/><font color='#555555'>Provide cleared source data</font>", styles["Body"]),
        Paragraph("<b>4) Save as .xml</b><br/><font color='#555555'>Use a plain-text editor</font>", styles["Body"]),
    ],
     [
        Paragraph("<b>5) Check the XML</b><br/><font color='#555555'>Review structure and values</font>", styles["Body"]),
        Paragraph("<b>6) Upload and review</b><br/><font color='#555555'>Check each entry in SciENcv</font>", styles["Body"]),
        Paragraph("<b>7) Certify</b><br/><font color='#555555'>The named person certifies</font>", styles["Body"]),
        Paragraph("<b>8) Save both files</b><br/><font color='#555555'>Uploaded XML and certified PDF</font>", styles["Body"]),
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

story.append(Paragraph("1) Check tool approval and prepare a safe draft", styles["H2"]))
story.append(Paragraph(
    "Use an institution-approved AI tool and share only information your institution permits you to use in that tool. "
    "Remove unnecessary personal or sensitive details from pasted text and attachments. Inputs may be retained by the vendor.",
    styles["Body"]
))
story.append(Spacer(1, 10))

callout = Table(
    [[Paragraph("<b>Review the draft</b>", styles["Tag"]),
      Paragraph(
          "Check the entries against the source records and verify the upload format against NLM's current guidance. "
          "Resolve missing facts with the investigator or sponsored programs office.",
          styles["Small"]
      )]],
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

story.append(Paragraph("2) Prepare the source records and changes", styles["H2"]))
story.append(Paragraph(
    "Use source records that reflect current and pending support. Identify the entries to add, edit, or remove.",
    styles["BodyMuted"]
))

story.append(Paragraph("Choose an input method", styles["H3"]))
inputs_list = ListFlowable(
    [
        ListItem(Paragraph("<b>Paste text.</b> Copy the permitted source entries and include column labels when copying a table.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Attach a file.</b> Confirm it is approved for use in the tool. Check that the draft follows the source table row by row.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Specify updates.</b> Give the source entries and a short list of requested changes in the same prompt.", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet",
    leftIndent=18,
    bulletFontName="Helvetica",
    bulletFontSize=10
)
story.append(inputs_list)
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_LINE, spaceBefore=6, spaceAfter=10))

story.append(Paragraph("3) Save the draft as plain-text XML", styles["H2"]))
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

story.append(Paragraph("Save the file", styles["H3"]))
save_steps = ListFlowable(
    [
        ListItem(Paragraph("<b>Copy the XML inside the code block.</b>", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Paste into a plain-text editor.</b> Use Notepad on Windows or choose <i>Format &gt; Make Plain Text</i> in macOS TextEdit.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("<b>Save the file with an .xml extension</b>, for example <span face='Courier'>OtherSupport.xml</span>. In Notepad, select <i>All Files</i> as the file type.", styles["Body"]), leftIndent=12),
    ],
    bulletType="1",
    start="1",
    leftIndent=18,
    bulletFontName="Helvetica",
    bulletFontSize=10
)
story.append(save_steps)

story.append(Spacer(1, 8))
story.append(Paragraph("Check the file before upload", styles["H3"]))
sanity = ListFlowable(
    [
        ListItem(Paragraph("File opens as readable text and starts with &lt;?xml or an opening XML tag.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Use straight quotes around XML attribute values. Keep Unicode punctuation in element text.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Use YYYY-MM-DD for support dates in the XML. If you only have a year, verify the month before completing the date in SciENcv.", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(sanity)

# ==================== PAGE 3 ====================
story.append(PageBreak())

story.append(Paragraph("4) Check, upload, and review", styles["H2"]))
story.append(Paragraph(
    "The playbook's browser validator is optional. It checks for common XML upload issues. Review all entries in SciENcv before certification.",
    styles["BodyMuted"]
))

story.append(Paragraph("Browser XML Validator", styles["H3"]))
story.append(Paragraph(
    '<link href="https://fritschelab.github.io/nih-sciencv-playbook/tools/" color="#0B3D91">https://fritschelab.github.io/nih-sciencv-playbook/tools/</link>',
    styles["Small"]
))

validator_steps = ListFlowable(
    [
        ListItem(Paragraph("Open the XML file or paste the XML into the editor.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Select <b>Validate</b> and address reported errors. Use <b>Format XML (clean)</b> if you need to make the XML easier to read.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("Select <b>Save XML</b> to download the file for upload.", styles["Body"]), leftIndent=12),
    ],
    bulletType="1", start="1", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(validator_steps)

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_LINE, spaceBefore=6, spaceAfter=10))

story.append(Paragraph("Upload to SciENcv and complete required fields", styles["H3"]))
upload_notes = ListFlowable(
    [
        ListItem(Paragraph("Upload the cleaned XML into SciENcv CPOS import.", styles["Body"]), leftIndent=12),
        ListItem(Paragraph("SciENcv may flag missing or incomplete fields (common: objectives, effort, dates). Fill or correct these in the SciENcv interface.", styles["Body"]), leftIndent=12),
    ],
    bulletType="bullet", leftIndent=18, bulletFontName="Helvetica", bulletFontSize=10
)
story.append(upload_notes)

story.append(Spacer(1, 10))
story.append(Paragraph("Review before certification", styles["H3"]))
review_box = Table(
    [[Paragraph(
        "<b>Quality control checklist</b><br/>"
        "1) Compare every imported entry line-by-line against the source Other Support document.<br/>"
        "2) Confirm totals, effort values, and dates (especially consultant roles).<br/>"
        "3) Have the named individual certify the CPOS in SciENcv from their own account.",
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
    "Save the uploaded XML and the certified CPOS PDF. Record any edits made after upload so the next update starts from the current record.",
    styles["Body"]
))

story.append(Spacer(1, 8))
story.append(Paragraph("Notes", styles["H3"]))
story.append(Paragraph(
    "This companion to the independent NIH Common Forms Playbook summarizes a drafting workflow. Follow NIH and NLM instructions for the current requirements.",
    styles["BodyMuted"]
))

doc.build(story)

out_path
