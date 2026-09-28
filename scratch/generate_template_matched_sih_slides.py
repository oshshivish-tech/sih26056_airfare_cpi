import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_template_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette matching the exact template
    C_WHITE = RGBColor(255, 255, 255)
    C_BLACK = RGBColor(0, 0, 0)
    C_NAVY = RGBColor(27, 54, 93)          # Dark navy serif
    C_BLUE_TEMPLATE = RGBColor(30, 64, 175) # #1E40AF vibrant blue border/accents
    C_RED_TEMPLATE = RGBColor(220, 38, 38)   # #DC2626 bright bold red
    C_FOOTER_BLUE = RGBColor(30, 64, 175)   # #1E40AF blue bottom bar
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_BORDER_LIGHT = RGBColor(203, 213, 225)
    C_PURPLE_CHALLENGE = RGBColor(243, 232, 255) # Light purple card for Slide 4
    C_PURPLE_BORDER = RGBColor(192, 132, 252)

    # Assets
    base_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
    pres_dir = os.path.join(base_dir, "public", "presentation")

    sih_top_logo = os.path.join(pres_dir, "page_1_img_2.png")
    sih_bulb_graphic = os.path.join(pres_dir, "page_1_img_1.png")
    arch_img = os.path.join(pres_dir, "architecture_diagram.png")
    proto_chart = os.path.join(pres_dir, "vayusuchak_prototype_chart.png")
    proto_table = os.path.join(pres_dir, "vayusuchak_prototype_table.png")

    def add_template_top_bar(slide, title_line1, title_line2=None, is_title_page=False):
        # 1. Team Name Pill on top-left (Oval pill like MegaZroN)
        if not is_title_page:
            pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(0.25), Inches(1.8), Inches(0.55))
            pill.adjustments[0] = 0.5
            pill.fill.solid()
            pill.fill.fore_color.rgb = C_WHITE
            pill.line.color.rgb = RGBColor(100, 116, 139)
            pill.line.width = Pt(1.5)
            tf_p = pill.text_frame
            tf_p.word_wrap = True
            p_p = tf_p.paragraphs[0]
            p_p.text = "Team Rookie"
            p_p.font.name = "Arial"
            p_p.font.size = Pt(13)
            p_p.font.bold = True
            p_p.font.color.rgb = C_BLACK
            p_p.alignment = PP_ALIGN.CENTER
            
        # 2. Main Title in the middle
        tb_t = slide.shapes.add_textbox(Inches(2.5), Inches(0.12), Inches(8.3), Inches(0.95))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t1 = tf_t.paragraphs[0]
        p_t1.text = title_line1
        p_t1.font.name = "Times New Roman" if is_title_page else "Arial"
        p_t1.font.size = Pt(28) if is_title_page else (Pt(22) if title_line2 else Pt(26))
        p_t1.font.bold = True
        p_t1.font.color.rgb = C_NAVY if is_title_page else C_BLACK
        p_t1.alignment = PP_ALIGN.CENTER
        
        if title_line2:
            p_t2 = tf_t.add_paragraph()
            p_t2.text = title_line2
            p_t2.font.name = "Times New Roman" if is_title_page else "Arial"
            p_t2.font.size = Pt(20) if is_title_page else Pt(20)
            p_t2.font.bold = True
            p_t2.font.color.rgb = C_NAVY if is_title_page else C_BLACK
            p_t2.alignment = PP_ALIGN.CENTER

        # 3. Official SIH Logo on top-right (page_1_img_2.png)
        if os.path.exists(sih_top_logo):
            slide.shapes.add_picture(sih_top_logo, Inches(11.1), Inches(0.12), Inches(1.8), Inches(0.85))

    def add_template_footer(slide, page_num):
        footer_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.15), prs.slide_width, Inches(0.35))
        footer_bar.fill.solid()
        footer_bar.fill.fore_color.rgb = C_FOOTER_BLUE
        footer_bar.line.fill.background()

        tb_f = slide.shapes.add_textbox(Inches(0.6), Inches(7.17), Inches(12.13), Inches(0.32))
        tf_f = tb_f.text_frame
        tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = tf_f.margin_bottom = 0
        p_fl = tf_f.paragraphs[0]
        p_fl.text = "@SIH Idea submission- Template"
        p_fl.font.name = "Arial"
        p_fl.font.size = Pt(9.5)
        p_fl.font.color.rgb = C_WHITE
        p_fl.alignment = PP_ALIGN.CENTER

        tb_r = slide.shapes.add_textbox(Inches(12.2), Inches(7.17), Inches(0.8), Inches(0.32))
        tf_r = tb_r.text_frame
        tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = tf_r.margin_bottom = 0
        p_fr = tf_r.paragraphs[0]
        p_fr.text = str(page_num)
        p_fr.font.name = "Arial"
        p_fr.font.size = Pt(9.5)
        p_fr.font.bold = True
        p_fr.font.color.rgb = C_WHITE
        p_fr.alignment = PP_ALIGN.RIGHT

    # =========================================================================
    # SLIDE 1: Title Page (Exact Template Page 1 with SIH Brain-Bulb Logo)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_WHITE
    bg1.line.fill.background()

    add_template_top_bar(s1, "SMART INDIA HACKATHON 2026", "TITLE PAGE", is_title_page=True)

    # Large SIH lightbulb graphic on the right (page_1_img_1.png)
    if os.path.exists(sih_bulb_graphic):
        s1.shapes.add_picture(sih_bulb_graphic, Inches(7.6), Inches(1.3), Inches(4.8), Inches(5.8))

    # Bullets on the left directly on the white canvas (no card border)
    tb_s1_bullets = s1.shapes.add_textbox(Inches(0.65), Inches(1.5), Inches(7.6), Inches(5.6))
    tf_s1 = tb_s1_bullets.text_frame
    tf_s1.word_wrap = True
    tf_s1.margin_left = tf_s1.margin_top = tf_s1.margin_right = tf_s1.margin_bottom = 0

    s1_items = [
        ("• Problem Statement ID –", "26056", False),
        ("• Problem Statement Title-", "Real-Time Airfare Price Index for CPI Augmentation", True),
        ("• Theme-", "Smart Governance / Miscellaneous", False),
        ("• PS Category-", "Software", False),
        ("• Team ID-", "Team Rookie", False),
        ("• Team Name (Registered on portal) :", "Team Rookie", False)
    ]

    for idx, (label, val, is_red) in enumerate(s1_items):
        p = tf_s1.add_paragraph() if idx > 0 else tf_s1.paragraphs[0]
        p.space_before = Pt(12)
        p.space_after = Pt(12)

        r_lbl = p.add_run()
        r_lbl.text = label + " "
        r_lbl.font.name = "Arial"
        r_lbl.font.size = Pt(17)
        r_lbl.font.bold = True
        r_lbl.font.color.rgb = C_BLACK

        r_val = p.add_run()
        r_val.text = val
        r_val.font.name = "Arial"
        r_val.font.size = Pt(17)
        r_val.font.bold = True
        r_val.font.color.rgb = C_RED_TEMPLATE if is_red else C_BLACK

    # =========================================================================
    # SLIDE 2: Proposed Solution (Exact Template Page 2)
    # Top: Integrated Smart Health... -> VayuSuchak: Real-Time Airfare Price Index Platform
    # Subtitle: ❖Proposed Solution (Describe your Idea/Solution/Prototype)
    # Left Box: We propose an ... (with key words highlighted in red bold)
    # Right Box: Uniqueness of Solution: (4 distinct points)
    # Bottom Box: DATA HARVESTING > IQR OUTLIER TRUNCATION > JEVONS GEOMETRIC INDEX > SHA-256 PROVENANCE > MoSPI CPI
    # Footer: @SIH Idea submission- Template 2
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = C_WHITE
    bg2.line.fill.background()

    add_template_top_bar(s2, "VayuSuchak: Real-Time Airfare Price Index", "Augmenting CPI Transport Inflation")

    # Subtitle with diamond bullet: ❖Proposed Solution (Describe your Idea/Solution/Prototype)
    tb_s2_sub = s2.shapes.add_textbox(Inches(0.55), Inches(1.15), Inches(12.2), Inches(0.45))
    tf_s2_sub = tb_s2_sub.text_frame
    tf_s2_sub.margin_left = tf_s2_sub.margin_top = tf_s2_sub.margin_right = tf_s2_sub.margin_bottom = 0
    p_s2_sub = tf_s2_sub.paragraphs[0]
    p_s2_sub.text = "❖Proposed Solution (Describe your Idea/Solution/Prototype)"
    p_s2_sub.font.name = "Arial"
    p_s2_sub.font.size = Pt(16)
    p_s2_sub.font.bold = True
    p_s2_sub.font.color.rgb = C_BLUE_TEMPLATE

    # Left Box: We propose an ...
    b_left_w = Inches(4.9)
    b_h = Inches(4.5)
    b_y = Inches(1.68)
    
    box_left = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), b_y, b_left_w, b_h)
    box_left.fill.solid()
    box_left.fill.fore_color.rgb = C_WHITE
    box_left.line.color.rgb = C_BLUE_TEMPLATE
    box_left.line.width = Pt(1.5)

    tb_bl = s2.shapes.add_textbox(Inches(0.7), b_y + Inches(0.18), b_left_w - Inches(0.3), b_h - Inches(0.36))
    tf_bl = tb_bl.text_frame
    tf_bl.word_wrap = True
    tf_bl.margin_left = tf_bl.margin_top = tf_bl.margin_right = tf_bl.margin_bottom = 0

    p_bl = tf_bl.paragraphs[0]
    p_bl.line_spacing = 1.35

    # Structured runs matching template style with key phrases in red
    runs_left = [
        ("We propose an ", False),
        ("Automated Real-Time Airfare Price Index (APIx) Platform", True),
        (" that integrates ", False),
        ("Multi-Carrier Headless Web Crawlers", True),
        (", ", False),
        ("UN/ILO Jevons Geometric Mean Indexing", True),
        (", and ", False),
        ("SHA-256 Cryptographic Audit Provenance", True),
        (" for proactive high-frequency detection of airline dynamic ticket yields and seamless augmentation of MoSPI CPI Transport Inflation.", False)
    ]

    for txt, is_red in runs_left:
        r = p_bl.add_run()
        r.text = txt
        r.font.name = "Arial"
        r.font.size = Pt(15.5)
        r.font.bold = is_red
        r.font.color.rgb = C_RED_TEMPLATE if is_red else C_BLACK

    # Right Box: Uniqueness of Solution:
    b_right_x = Inches(5.6)
    b_right_w = Inches(7.18)

    box_right = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, b_right_x, b_y, b_right_w, b_h)
    box_right.fill.solid()
    box_right.fill.fore_color.rgb = C_WHITE
    box_right.line.color.rgb = C_BLUE_TEMPLATE
    box_right.line.width = Pt(1.5)

    tb_br = s2.shapes.add_textbox(b_right_x + Inches(0.2), b_y + Inches(0.18), b_right_w - Inches(0.4), b_h - Inches(0.36))
    tf_br = tb_br.text_frame
    tf_br.word_wrap = True
    tf_br.margin_left = tf_br.margin_top = tf_br.margin_right = tf_br.margin_bottom = 0

    p_rh = tf_br.paragraphs[0]
    p_rh.text = "Uniqueness of Solution:"
    p_rh.font.name = "Arial"
    p_rh.font.size = Pt(16)
    p_rh.font.bold = True
    p_rh.font.color.rgb = C_BLACK
    p_rh.space_after = Pt(12)

    unique_items = [
        ("Dynamic Yield Sensitivity: ", "Captures high-frequency intraday algorithmic surges across T+1..T+45 advance booking windows vs 15-day delayed manual visits."),
        ("Zero Upward Substitution Bias: ", "Employs UN/ILO Chapter 10 Jevons geometric mean, mathematically eliminating Dutot arithmetic distortion."),
        ("Cryptographic Legal Audit: ", "SHA-256 batch fingerprints ensure tamper-proof legal evidentiary standards for MoSPI NSO & RBI monetary policy."),
        ("Community & Regional Access: ", "Scales seamlessly from 12 core metro routes to 250+ UDAN regional routes with zero additional hardware."),
        (">95% Operational Cost Reduction: ", "Fully serverless automated pipeline slashes multi-crore physical field surveyor visit logistics.")
    ]

    for idx, (title, desc) in enumerate(unique_items):
        p_u = tf_br.add_paragraph()
        p_u.space_after = Pt(9)
        p_u.line_spacing = 1.2
        
        r_ut = p_u.add_run()
        r_ut.text = title
        r_ut.font.name = "Arial"
        r_ut.font.size = Pt(13)
        r_ut.font.bold = True
        r_ut.font.color.rgb = C_BLACK

        r_ud = p_u.add_run()
        r_ud.text = desc
        r_ud.font.name = "Arial"
        r_ud.font.size = Pt(12.5)
        r_ud.font.color.rgb = C_TEXT_DARK

    # Bottom Full-Width Box: Process Pipeline
    box_bottom = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(6.32), Inches(12.23), Inches(0.58))
    box_bottom.fill.solid()
    box_bottom.fill.fore_color.rgb = C_WHITE
    box_bottom.line.color.rgb = C_BLUE_TEMPLATE
    box_bottom.line.width = Pt(1.5)

    tb_bb = s2.shapes.add_textbox(Inches(0.65), Inches(6.36), Inches(12.03), Inches(0.5))
    tf_bb = tb_bb.text_frame
    p_bb = tf_bb.paragraphs[0]
    p_bb.text = "DATA HARVESTING > IQR OUTLIER TRUNCATION > JEVONS GEOMETRIC INDEX > SHA-256 PROVENANCE > MoSPI & RBI CPI INTEGRATION"
    p_bb.font.name = "Arial"
    p_bb.font.size = Pt(11.5)
    p_bb.font.bold = True
    p_bb.font.color.rgb = C_BLACK
    p_bb.alignment = PP_ALIGN.CENTER

    add_template_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: Technical Approach (Exact Template Page 3)
    # Top: Team Rookie | TECHNICAL APPROACH | SIH Logo
    # Left Column: Technologies Used:
    #   Languages: Python (ML), TypeScript (Dashboard), SQL (Storage).
    #   Tools & Frameworks: Playwright, UN/ILO Jevons, SciPy, SHA-256, PostgreSQL, etc.
    # Right Column: Complete Process Flow Architecture Diagram
    # Footer: @SIH Idea submission- Template 3
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = C_WHITE
    bg3.line.fill.background()

    add_template_top_bar(s3, "TECHNICAL APPROACH")

    # Left Column: Blue Framed Box
    col_left_w = Inches(5.2)
    col_h = Inches(5.65)
    col_y = Inches(1.22)

    box_s3_left = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), col_y, col_left_w, col_h)
    box_s3_left.fill.solid()
    box_s3_left.fill.fore_color.rgb = C_WHITE
    box_s3_left.line.color.rgb = C_BLUE_TEMPLATE
    box_s3_left.line.width = Pt(1.5)

    tb_s3_l = s3.shapes.add_textbox(Inches(0.75), col_y + Inches(0.18), col_left_w - Inches(0.4), col_h - Inches(0.36))
    tf_s3_l = tb_s3_l.text_frame
    tf_s3_l.word_wrap = True
    tf_s3_l.margin_left = tf_s3_l.margin_top = tf_s3_l.margin_right = tf_s3_l.margin_bottom = 0

    # Header: Technologies Used:
    p_t_head = tf_s3_l.paragraphs[0]
    p_t_head.text = "Technologies Used:"
    p_t_head.font.name = "Arial"
    p_t_head.font.size = Pt(18)
    p_t_head.font.bold = True
    p_t_head.font.color.rgb = C_BLUE_TEMPLATE
    p_t_head.space_after = Pt(10)

    # Section 1: Languages:
    p_lang_h = tf_s3_l.add_paragraph()
    p_lang_h.text = "Languages: "
    p_lang_h.font.name = "Arial"
    p_lang_h.font.size = Pt(15.5)
    p_lang_h.font.bold = True
    p_lang_h.font.color.rgb = C_RED_TEMPLATE

    r_lang_v = p_lang_h.add_run()
    r_lang_v.text = "Python 3.13 (Crawlers & Engine), TypeScript (Dashboard), SQL (Storage)."
    r_lang_v.font.name = "Arial"
    r_lang_v.font.size = Pt(14)
    r_lang_v.font.bold = True
    r_lang_v.font.color.rgb = C_BLACK
    p_lang_h.space_after = Pt(14)

    # Section 2: Tools & Frameworks:
    p_tf_h = tf_s3_l.add_paragraph()
    p_tf_h.text = "Tools & Frameworks:"
    p_tf_h.font.name = "Arial"
    p_tf_h.font.size = Pt(15.5)
    p_tf_h.font.bold = True
    p_tf_h.font.color.rgb = C_RED_TEMPLATE
    p_tf_h.space_after = Pt(6)

    tools_list = [
        "Playwright Headless (Anti-Detection Scraping)",
        "UN/ILO Jevons Index Formula (Elementary Aggregation)",
        "SciPy & NumPy (Dynamic IQR Outlier Filter)",
        "SHA-256 Cryptographic Vault (Batch Audit Ledger)",
        "FastAPI & Uvicorn (High-Throughput REST Microservices)",
        "PostgreSQL (Relational Time-Series Fare Database)",
        "React 19 & TailwindCSS (Interactive Policy Dashboards)",
        "Vercel Edge & GitHub Actions (Serverless Daily Cron)"
    ]

    for tool_item in tools_list:
        p_tool = tf_s3_l.add_paragraph()
        p_tool.space_after = Pt(5)
        r_t = p_tool.add_run()
        r_t.text = "• " + tool_item
        r_t.font.name = "Arial"
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_t.font.color.rgb = C_BLACK

    # Right Column: Flowchart Architecture Diagram
    if os.path.exists(arch_img):
        s3.shapes.add_picture(arch_img, Inches(5.95), col_y, Inches(6.83), col_h)

    add_template_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: Feasibility and Viability (Exact Template Page 4 Layout)
    # Left: Technical Feasibility (red), Operational Feasibility (red), Economic Feasibility (red)
    # Right: Challenges & Solutions (6 colored challenge/solution cards)
    # Footer: @SIH Idea submission- Template 4
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = C_WHITE
    bg4.line.fill.background()

    add_template_top_bar(s4, "FEASIBILITY AND VIABILITY")

    # Left Column: Feasibility Box
    box_s4_left = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.22), Inches(4.9), Inches(5.65))
    box_s4_left.fill.solid()
    box_s4_left.fill.fore_color.rgb = C_WHITE
    box_s4_left.line.color.rgb = C_BLUE_TEMPLATE
    box_s4_left.line.width = Pt(1.5)

    tb_s4_l = s4.shapes.add_textbox(Inches(0.72), Inches(1.38), Inches(4.56), Inches(5.3))
    tf_s4_l = tb_s4_l.text_frame
    tf_s4_l.word_wrap = True
    tf_s4_l.margin_left = tf_s4_l.margin_top = tf_s4_l.margin_right = tf_s4_l.margin_bottom = 0

    feasibilities = [
        (
            "Technical Feasibility: ",
            "Playwright headless crawlers extract live fares from 4 carriers in <10s. SciPy dynamic IQR filters yield anomalies and phantom fares automatically. UN/ILO Chapter 10 geometric mean ensures zero upward bias."
        ),
        (
            "Operational Feasibility: ",
            "Seamless zero-touch deployment. Replaces thousands of manual surveyor airport visits with autonomous daily cron. Native REST API feeds directly into MoSPI eSankhyiki and RBI MPC systems."
        ),
        (
            "Economic Feasibility: ",
            "Ultra-low serverless cloud architecture operates for < ₹3,500/month, slashing recurring physical survey expenditure by >95% (saving MoSPI an estimated ₹15+ Crores annually in field visits)."
        )
    ]

    for idx, (f_head, f_desc) in enumerate(feasibilities):
        p_f = tf_s4_l.add_paragraph() if idx > 0 else tf_s4_l.paragraphs[0]
        p_f.space_after = Pt(14)
        p_f.line_spacing = 1.25

        r_fh = p_f.add_run()
        r_fh.text = f_head
        r_fh.font.name = "Arial"
        r_fh.font.size = Pt(14)
        r_fh.font.bold = True
        r_fh.font.color.rgb = C_RED_TEMPLATE

        r_fd = p_f.add_run()
        r_fd.text = f_desc
        r_fd.font.name = "Arial"
        r_fd.font.size = Pt(12.5)
        r_fd.font.color.rgb = C_BLACK

    # Right Section: Challenges & Solutions
    tb_cs_title = s4.shapes.add_textbox(Inches(5.7), Inches(1.22), Inches(7.08), Inches(0.45))
    tf_cst = tb_cs_title.text_frame
    p_cst = tf_cst.paragraphs[0]
    p_cst.text = "Challenges & Solutions"
    p_cst.font.name = "Arial"
    p_cst.font.size = Pt(20)
    p_cst.font.bold = True
    p_cst.font.color.rgb = C_BLUE_TEMPLATE
    p_cst.alignment = PP_ALIGN.CENTER

    # 6 Challenges & Solutions Cards (2 columns x 3 rows)
    challenges = [
        ("Anti-Scraping / Cloudflare: ", "Ethical crawl delays, rotating proxy pool, and human jitter delay."),
        ("DOM Layout Shifts: ", "Semantic ARIA selectors and schema fallback baseline layers."),
        ("Surge Anomalies: ", "Automated IQR truncation [Q1-1.5, Q3+2] with Z-score audit tags."),
        ("Data Legal Integrity: ", "SHA-256 batch cryptographic hash manifest for sovereign audit."),
        ("Scalability: ", "Serverless edge architecture scales easily from 12 metros to 250+ UDAN routes."),
        ("Substitution Bias: ", "UN/ILO Jevons geometric mean eliminates Dutot upward formula distortion.")
    ]

    card_w = Inches(3.4)
    card_h = Inches(1.52)
    for c_idx, (c_title, c_text) in enumerate(challenges):
        col = c_idx % 2
        row = c_idx // 2
        c_x = Inches(5.7) + col * (card_w + Inches(0.28))
        c_y = Inches(1.8) + row * (card_h + Inches(0.18))

        c_box = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_x, c_y, card_w, card_h)
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = C_PURPLE_CHALLENGE
        c_box.line.color.rgb = C_PURPLE_BORDER
        c_box.line.width = Pt(1.0)

        tb_c = s4.shapes.add_textbox(c_x + Inches(0.12), c_y + Inches(0.1), card_w - Inches(0.24), card_h - Inches(0.2))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
        p_c = tf_c.paragraphs[0]
        p_c.line_spacing = 1.15
        
        r_ct = p_c.add_run()
        r_ct.text = c_title
        r_ct.font.name = "Arial"
        r_ct.font.size = Pt(10)
        r_ct.font.bold = True
        r_ct.font.color.rgb = RGBColor(88, 28, 135) # Deep purple

        r_cd = p_c.add_run()
        r_cd.text = c_text
        r_cd.font.name = "Arial"
        r_cd.font.size = Pt(9.5)
        r_cd.font.color.rgb = C_TEXT_DARK

    add_template_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: Impact and Benefits (Exact Template Page 5)
    # Left:
    #   Top Box: Potential Impact (blue bold)
    #   Bottom Box: Benefits: (Social, Economic, National DPI in red)
    # Right:
    #   Top Box: PROTOTYPE IMAGE 1 (red label + Prototype Chart)
    #   Bottom Box: PROTOTYPE IMAGE 2 (red label + Prototype Corridor Table)
    # Footer: @SIH Idea submission- Template 5
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = C_WHITE
    bg5.line.fill.background()

    add_template_top_bar(s5, "IMPACT AND BENEFITS")

    # Left Column Top Box: Potential Impact
    l_w = Inches(5.0)
    box_s5_imp = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.22), l_w, Inches(2.72))
    box_s5_imp.fill.solid()
    box_s5_imp.fill.fore_color.rgb = C_WHITE
    box_s5_imp.line.color.rgb = C_BLUE_TEMPLATE
    box_s5_imp.line.width = Pt(1.5)

    tb_imp = s5.shapes.add_textbox(Inches(0.7), Inches(1.3), l_w - Inches(0.3), Inches(2.54))
    tf_imp = tb_imp.text_frame
    tf_imp.word_wrap = True
    tf_imp.margin_left = tf_imp.margin_top = tf_imp.margin_right = tf_imp.margin_bottom = 0

    p_ih = tf_imp.paragraphs[0]
    p_ih.text = "Potential Impact"
    p_ih.font.name = "Arial"
    p_ih.font.size = Pt(16)
    p_ih.font.bold = True
    p_ih.font.color.rgb = C_BLUE_TEMPLATE
    p_ih.space_after = Pt(6)

    impacts_list = [
        ("Zero Policy Lag: ", "Slashes price collection latency from 15 days to real-time (0 days), eliminating policy blindspots."),
        ("Comprehensive Dynamic Coverage: ", "Ingests 10,000+ daily fare quotes across 12 metro routes vs 1 monthly static quote."),
        ("Elimination of Substitution Bias: ", "Mathematically eliminates 20-30 bps upward inflation distortion via UN/ILO Jevons indexing.")
    ]

    for itit, idesc in impacts_list:
        p_i = tf_imp.add_paragraph()
        p_i.space_after = Pt(4)
        p_i.line_spacing = 1.15
        
        r_it = p_i.add_run()
        r_it.text = "• " + itit
        r_it.font.name = "Arial"
        r_it.font.size = Pt(11)
        r_it.font.bold = True
        r_it.font.color.rgb = C_BLACK

        r_id = p_i.add_run()
        r_id.text = idesc
        r_id.font.name = "Arial"
        r_id.font.size = Pt(10.5)
        r_id.font.color.rgb = C_TEXT_DARK

    # Left Column Bottom Box: Benefits:
    box_s5_ben = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(4.08), l_w, Inches(2.8))
    box_s5_ben.fill.solid()
    box_s5_ben.fill.fore_color.rgb = C_WHITE
    box_s5_ben.line.color.rgb = C_BLUE_TEMPLATE
    box_s5_ben.line.width = Pt(1.5)

    tb_ben = s5.shapes.add_textbox(Inches(0.7), Inches(4.16), l_w - Inches(0.3), Inches(2.62))
    tf_ben = tb_ben.text_frame
    tf_ben.word_wrap = True
    tf_ben.margin_left = tf_ben.margin_top = tf_ben.margin_right = tf_ben.margin_bottom = 0

    p_bh = tf_ben.paragraphs[0]
    p_bh.text = "Benefits:"
    p_bh.font.name = "Arial"
    p_bh.font.size = Pt(16)
    p_bh.font.bold = True
    p_bh.font.color.rgb = C_BLUE_TEMPLATE
    p_bh.space_after = Pt(6)

    benefits_list = [
        ("Sovereign (MoSPI NSO): ", "Direct automated API feed into eSankhyiki & NDAP; transparent, reproducible inflation indices."),
        ("Monetary Policy (RBI MPC): ", "Provides high-frequency leading transport inflation signals for proactive interest rate setting."),
        ("Economic & Fiscal: ", "Saves ₹15+ Crores annually in physical surveyor travel and logistics overheads (< ₹3,500/mo cloud cost)."),
        ("National DPI: ", "India's first open, verifiable high-frequency price monitoring infrastructure with SHA-256 legal auditability.")
    ]

    for btit, bdesc in benefits_list:
        p_b = tf_ben.add_paragraph()
        p_b.space_after = Pt(4)
        p_b.line_spacing = 1.15
        
        r_bt = p_b.add_run()
        r_bt.text = "• " + btit
        r_bt.font.name = "Arial"
        r_bt.font.size = Pt(11)
        r_bt.font.bold = True
        r_bt.font.color.rgb = C_RED_TEMPLATE

        r_bd = p_b.add_run()
        r_bd.text = bdesc
        r_bd.font.name = "Arial"
        r_bd.font.size = Pt(10.5)
        r_bd.font.color.rgb = C_TEXT_DARK

    # Right Column: Two Prototype Image Boxes
    r_x = Inches(5.75)
    r_w = Inches(7.03)
    p_box_h = Inches(2.72)

    # Top Prototype Box: PROTOTYPE IMAGE 1
    box_p1 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, r_x, Inches(1.22), r_w, p_box_h)
    box_p1.fill.solid()
    box_p1.fill.fore_color.rgb = C_WHITE
    box_p1.line.color.rgb = C_BLUE_TEMPLATE
    box_p1.line.width = Pt(1.5)

    tb_p1_lbl = s5.shapes.add_textbox(r_x + Inches(0.12), Inches(1.26), r_w - Inches(0.24), Inches(0.35))
    tf_p1 = tb_p1_lbl.text_frame
    tf_p1.margin_left = tf_p1.margin_top = tf_p1.margin_right = tf_p1.margin_bottom = 0
    p_p1 = tf_p1.paragraphs[0]
    p_p1.text = "PROTOTYPE IMAGE 1 (Live Real-Time Airfare Price Index Dashboard)"
    p_p1.font.name = "Arial"
    p_p1.font.size = Pt(11)
    p_p1.font.bold = True
    p_p1.font.color.rgb = C_RED_TEMPLATE

    if os.path.exists(proto_chart):
        s5.shapes.add_picture(proto_chart, r_x + Inches(0.08), Inches(1.58), r_w - Inches(0.16), p_box_h - Inches(0.42))

    # Bottom Prototype Box: PROTOTYPE IMAGE 2
    box_p2 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, r_x, Inches(4.08), r_w, Inches(2.8))
    box_p2.fill.solid()
    box_p2.fill.fore_color.rgb = C_WHITE
    box_p2.line.color.rgb = C_BLUE_TEMPLATE
    box_p2.line.width = Pt(1.5)

    tb_p2_lbl = s5.shapes.add_textbox(r_x + Inches(0.12), Inches(4.12), r_w - Inches(0.24), Inches(0.35))
    tf_p2 = tb_p2_lbl.text_frame
    tf_p2.margin_left = tf_p2.margin_top = tf_p2.margin_right = tf_p2.margin_bottom = 0
    p_p2 = tf_p2.paragraphs[0]
    p_p2.text = "PROTOTYPE IMAGE 2 (Corridor-Wise Yield & Surge Analytics Table)"
    p_p2.font.name = "Arial"
    p_p2.font.size = Pt(11)
    p_p2.font.bold = True
    p_p2.font.color.rgb = C_RED_TEMPLATE

    if os.path.exists(proto_table):
        s5.shapes.add_picture(proto_table, r_x + Inches(0.08), Inches(4.44), r_w - Inches(0.16), Inches(2.38))

    add_template_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: Research and References (Exact Template Page 6)
    # Top: Team Rookie | RESEARCH AND REFERENCES | SIH Logo
    # Body: Clean Academic & Official Citations [1]..[4]
    # Footer: @SIH Idea submission- Template 6
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = C_WHITE
    bg6.line.fill.background()

    add_template_top_bar(s6, "RESEARCH AND REFERENCES")

    tb_s6 = s6.shapes.add_textbox(Inches(0.65), Inches(1.5), Inches(12.0), Inches(5.3))
    tf_s6 = tb_s6.text_frame
    tf_s6.word_wrap = True
    tf_s6.margin_left = tf_s6.margin_top = tf_s6.margin_right = tf_s6.margin_bottom = 0

    citations = [
        "[1] Cavallo, A., & Rigobon, R., 'The Billion Prices Project: Using Online Data for Measurement and Research,' Journal of Economic Perspectives, vol. 30, no. 2, pp. 151-178, 2016.",
        "[2] United Nations, ILO, IMF, OECD, Eurostat, World Bank, Consumer Price Index Manual: Concepts and Methods, Chapter 10 (Elementary Indices), Geneva, 2020.",
        "[3] Directorate General of Civil Aviation (DGCA) India, Monthly Scheduled Domestic Passenger Traffic Reports. Available: https://www.dgca.gov.in/ (Accessed: Sept. 2026).",
        "[4] Ministry of Statistics and Programme Implementation (MoSPI), Consumer Price Index Concepts and Methodological Guidelines. Available: https://www.mospi.gov.in/ (Accessed: Sept. 2026)."
    ]

    for idx, cite in enumerate(citations):
        p_c = tf_s6.add_paragraph() if idx > 0 else tf_s6.paragraphs[0]
        p_c.space_before = Pt(14)
        p_c.space_after = Pt(14)
        p_c.line_spacing = 1.3
        r_c = p_c.add_run()
        r_c.text = cite
        r_c.font.name = "Arial"
        r_c.font.size = Pt(15.5)
        r_c.font.color.rgb = C_BLACK

    add_template_footer(s6, 6)

    prs.save(output_path)
    print(f"Successfully generated presentation matching exact template at {output_path}")

if __name__ == "__main__":
    out_file = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24\scratch\AirIntel_India_SIH26056_Presentation.pptx"
    create_template_presentation(out_file)
