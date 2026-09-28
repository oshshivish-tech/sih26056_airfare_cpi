import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def test_slide_3():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    C_WHITE = RGBColor(255, 255, 255)
    C_BLACK = RGBColor(0, 0, 0)
    C_NAVY = RGBColor(27, 54, 93)
    C_BLUE_TEMPLATE = RGBColor(30, 64, 175)
    C_RED_TEMPLATE = RGBColor(220, 38, 38)
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(71, 85, 105)

    base_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
    pres_dir = os.path.join(base_dir, "public", "presentation")
    sih_top_logo = os.path.join(pres_dir, "page_1_img_2.png")
    arch_img = os.path.join(pres_dir, "architecture_diagram.png")

    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = C_WHITE
    bg3.line.fill.background()

    # 1. Top Bar: Roorkies Pill, Title, SIH Logo
    pill = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(0.20), Inches(1.8), Inches(0.55))
    pill.adjustments[0] = 0.5
    pill.fill.solid()
    pill.fill.fore_color.rgb = C_WHITE
    pill.line.color.rgb = RGBColor(100, 116, 139)
    pill.line.width = Pt(1.5)
    tf_p = pill.text_frame
    tf_p.word_wrap = True
    p_p = tf_p.paragraphs[0]
    p_p.text = "Roorkies"
    p_p.font.name = "Arial"
    p_p.font.size = Pt(13)
    p_p.font.bold = True
    p_p.font.color.rgb = C_BLACK
    p_p.alignment = PP_ALIGN.CENTER

    tb_t = s3.shapes.add_textbox(Inches(2.5), Inches(0.12), Inches(8.3), Inches(0.95))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "TECHNICAL APPROACH & ARCHITECTURE"
    p_t1.font.name = "Times New Roman"
    p_t1.font.size = Pt(25)
    p_t1.font.bold = True
    p_t1.font.color.rgb = C_NAVY
    p_t1.alignment = PP_ALIGN.CENTER

    if os.path.exists(sih_top_logo):
        s3.shapes.add_picture(sih_top_logo, Inches(11.1), Inches(0.12), Inches(1.8), Inches(0.85))

    col_y = Inches(1.15)
    col_h = Inches(5.95)

    # 2. Left Column: Categorized Technology Stack (Width: 3.85 inches)
    col_w_l = Inches(3.85)
    box_l = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), col_y, col_w_l, col_h)
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = RGBColor(248, 250, 252) # soft slate-50
    box_l.line.color.rgb = C_BLUE_TEMPLATE
    box_l.line.width = Pt(1.5)

    tb_l = s3.shapes.add_textbox(Inches(0.70), col_y + Inches(0.12), col_w_l - Inches(0.30), col_h - Inches(0.24))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p_lh = tf_l.paragraphs[0]
    p_lh.text = "Technologies Used:"
    p_lh.font.name = "Arial"
    p_lh.font.size = Pt(16)
    p_lh.font.bold = True
    p_lh.font.color.rgb = C_BLUE_TEMPLATE
    p_lh.space_after = Pt(8)

    tech_sections = [
        (
            "Languages & Runtimes:",
            RGBColor(220, 38, 38),
            [
                "Python 3.13 (Async Harvester & Engine)",
                "TypeScript & React 19 (Dashboard UI)",
                "SQL (PostgreSQL Time-Series & SQLite)"
            ]
        ),
        (
            "Extraction & Cleansing:",
            RGBColor(30, 64, 175),
            [
                "Playwright Headless (Anti-Bot Crawlers)",
                "SciPy & NumPy (Dynamic IQR Filter)"
            ]
        ),
        (
            "Index Calculation & Crypto:",
            RGBColor(124, 58, 237),
            [
                "UN/ILO Jevons Index Formula (GMI)",
                "SHA-256 Batch Merkle Audit Ledger"
            ]
        ),
        (
            "API, Cloud & Standards:",
            RGBColor(16, 185, 129),
            [
                "FastAPI & Uvicorn (Sub-10ms REST APIs)",
                "Vercel Edge & GitHub Actions Cron",
                "NDSAP Open Data & UN/ILO Ch. 10"
            ]
        )
    ]

    for sec_title, sec_color, sec_items in tech_sections:
        p_sec = tf_l.add_paragraph()
        p_sec.space_before = Pt(6)
        p_sec.space_after = Pt(2)
        r_sec = p_sec.add_run()
        r_sec.text = sec_title
        r_sec.font.name = "Arial"
        r_sec.font.size = Pt(11)
        r_sec.font.bold = True
        r_sec.font.color.rgb = sec_color

        for item in sec_items:
            p_item = tf_l.add_paragraph()
            p_item.space_after = Pt(2.5)
            r_dot = p_item.add_run()
            r_dot.text = "• "
            r_dot.font.name = "Arial"
            r_dot.font.size = Pt(9.5)
            r_dot.font.bold = True
            r_dot.font.color.rgb = C_TEXT_DARK

            r_txt = p_item.add_run()
            r_txt.text = item
            r_txt.font.name = "Arial"
            r_txt.font.size = Pt(9.2)
            r_txt.font.bold = False
            r_txt.font.color.rgb = C_TEXT_DARK

    # 3. Right Top Section: Architecture Flowchart (Width: 8.23 inches)
    flow_x = Inches(4.55)
    flow_w = Inches(8.23)
    flow_h = Inches(3.55)

    if os.path.exists(arch_img):
        s3.shapes.add_picture(arch_img, flow_x, col_y, flow_w, flow_h)

    # 4. Underneath Flowchart: Non-Repetitive Engineering Deep-Dives
    sub_y = col_y + flow_h + Inches(0.12)
    sub_h = col_h - flow_h - Inches(0.12) # ~2.28 inches
    card_w = Inches(4.04)

    # --- Card A: Mathematical Formulation & Axiomatic Rigor ---
    card_a = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, flow_x, sub_y, card_w, sub_h)
    card_a.fill.solid()
    card_a.fill.fore_color.rgb = RGBColor(240, 249, 255) # soft sky-50
    card_a.line.color.rgb = RGBColor(2, 132, 199)
    card_a.line.width = Pt(1.4)

    tb_ca = s3.shapes.add_textbox(flow_x + Inches(0.14), sub_y + Inches(0.10), card_w - Inches(0.28), sub_h - Inches(0.20))
    tf_ca = tb_ca.text_frame
    tf_ca.word_wrap = True
    tf_ca.margin_left = tf_ca.margin_top = tf_ca.margin_right = tf_ca.margin_bottom = 0

    p_cah = tf_ca.paragraphs[0]
    p_cah.text = "📐 Mathematical Formulation (UN/ILO Ch. 10)"
    p_cah.font.name = "Arial"
    p_cah.font.size = Pt(11)
    p_cah.font.bold = True
    p_cah.font.color.rgb = RGBColor(2, 132, 199)
    p_cah.space_after = Pt(4)

    math_pts = [
        ("Elementary Jevons Geometric Mean:", " J = ∏ (pt,i / p0,i)^(1/n)"),
        ("Axiomatic Proof:", " Eliminates Dutot arithmetic upward substitution bias (~25 bps distortion removed)."),
        ("DGCA Laspeyres Aggregation:", " It = ∑ Wr · Jr,t across corridors weighted by official passenger volume shares.")
    ]
    for m_head, m_desc in math_pts:
        p = tf_ca.add_paragraph()
        p.space_after = Pt(3.5)
        p.line_spacing = 1.15
        r1 = p.add_run()
        r1.text = "• " + m_head
        r1.font.name = "Arial"
        r1.font.size = Pt(9.2)
        r1.font.bold = True
        r1.font.color.rgb = C_BLACK
        r2 = p.add_run()
        r2.text = m_desc
        r2.font.name = "Arial"
        r2.font.size = Pt(8.8)
        r2.font.color.rgb = C_TEXT_DARK

    # --- Card B: System Benchmarks & Engineering SLAs ---
    card_b_x = flow_x + card_w + Inches(0.15)
    card_b = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, card_b_x, sub_y, card_w, sub_h)
    card_b.fill.solid()
    card_b.fill.fore_color.rgb = RGBColor(240, 253, 244) # soft emerald-50
    card_b.line.color.rgb = RGBColor(22, 163, 74)
    card_b.line.width = Pt(1.4)

    tb_cb = s3.shapes.add_textbox(card_b_x + Inches(0.14), sub_y + Inches(0.10), card_w - Inches(0.28), sub_h - Inches(0.20))
    tf_cb = tb_cb.text_frame
    tf_cb.word_wrap = True
    tf_cb.margin_left = tf_cb.margin_top = tf_cb.margin_right = tf_cb.margin_bottom = 0

    p_cbh = tf_cb.paragraphs[0]
    p_cbh.text = "⚙️ Production Benchmarks & Engineering SLAs"
    p_cbh.font.name = "Arial"
    p_cbh.font.size = Pt(11)
    p_cbh.font.bold = True
    p_cbh.font.color.rgb = RGBColor(21, 128, 61)
    p_cbh.space_after = Pt(4)

    eng_pts = [
        ("Harvester Throughput:", " 10,000+ daily live quotes captured across 12 sectors in under 18 minutes."),
        ("Dynamic IQR Outlier Filter:", " SciPy dynamically purges bottom 2.5% phantom taxes and top 5% surge anomalies."),
        ("Sub-10ms REST API:", " Fully automated JSON/CSV endpoints ready for MoSPI eSankhyiki & RBI integration.")
    ]
    for e_head, e_desc in eng_pts:
        p = tf_cb.add_paragraph()
        p.space_after = Pt(3.5)
        p.line_spacing = 1.15
        r1 = p.add_run()
        r1.text = "• " + e_head
        r1.font.name = "Arial"
        r1.font.size = Pt(9.2)
        r1.font.bold = True
        r1.font.color.rgb = C_BLACK
        r2 = p.add_run()
        r2.text = e_desc
        r2.font.name = "Arial"
        r2.font.size = Pt(8.8)
        r2.font.color.rgb = C_TEXT_DARK

    out_pptx = os.path.join(base_dir, "scratch", "test_slide_3_clean.pptx")
    prs.save(out_pptx)
    print("Saved test pptx to", out_pptx)

    # Export via COM
    import win32com.client
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    pres_com = ppt.Presentations.Open(os.path.abspath(out_pptx), False, False, False)
    out_png = os.path.join(base_dir, "scratch", "test_slide_3_clean.png")
    pres_com.Slides(1).Export(out_png, "PNG", 1920, 1080)
    pres_com.Close()
    ppt.Quit()
    print("Exported test png to", out_png)

if __name__ == "__main__":
    test_slide_3()
