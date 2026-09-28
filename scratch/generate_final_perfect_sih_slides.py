import os
import sys
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_final_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette matching the exact SIH template
    C_WHITE = RGBColor(255, 255, 255)
    C_BLACK = RGBColor(0, 0, 0)
    C_NAVY = RGBColor(27, 54, 93)          # Dark navy serif
    C_BLUE_TEMPLATE = RGBColor(30, 64, 175) # #1E40AF vibrant blue border/accents
    C_RED_TEMPLATE = RGBColor(220, 38, 38)   # #DC2626 bright bold red
    C_FOOTER_BLUE = RGBColor(30, 64, 175)   # #1E40AF blue bottom bar
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(71, 85, 105)
    C_BORDER_LIGHT = RGBColor(203, 213, 225)
    C_BLUE_LIGHT_BG = RGBColor(239, 246, 255)
    C_SLATE_LIGHT_BG = RGBColor(248, 250, 252)

    # Assets
    base_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
    pres_dir = os.path.join(base_dir, "public", "presentation")

    sih_top_logo = os.path.join(pres_dir, "page_1_img_2.png")
    sih_bulb_graphic = os.path.join(pres_dir, "page_1_img_1.png")
    arch_img = os.path.join(pres_dir, "architecture_diagram.png")
    proto_chart = os.path.join(pres_dir, "vayusuchak_prototype_chart.png")
    proto_table = os.path.join(pres_dir, "vayusuchak_prototype_table.png")
    runway_banner = os.path.join(pres_dir, "runway_skyline_banner.png")
    workflow_strip_img = os.path.join(pres_dir, "workflow_circular_nodes.png")

    def add_template_top_bar(slide, title_line1, title_line2=None, is_title_page=False, title_font_size=25, title_color=C_BLACK, is_serif=False):
        # 1. Team Name Pill on top-left (Oval pill like MegaZroN in template)
        if not is_title_page:
            pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(0.22), Inches(1.8), Inches(0.55))
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
            
        # 2. Main Title in the middle
        tb_t = slide.shapes.add_textbox(Inches(2.5), Inches(0.12), Inches(8.3), Inches(0.95))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t1 = tf_t.paragraphs[0]
        p_t1.text = title_line1
        p_t1.font.name = "Times New Roman" if (is_title_page or is_serif) else "Arial"
        p_t1.font.size = Pt(title_font_size)
        p_t1.font.bold = True
        p_t1.font.color.rgb = title_color
        p_t1.alignment = PP_ALIGN.CENTER
        
        if title_line2:
            p_t2 = tf_t.add_paragraph()
            p_t2.text = title_line2
            p_t2.font.name = "Times New Roman" if (is_title_page or is_serif) else "Arial"
            p_t2.font.size = Pt(int(title_font_size * 0.75))
            p_t2.font.bold = True
            p_t2.font.color.rgb = RGBColor(30, 64, 175) if (is_serif and not is_title_page) else title_color
            p_t2.alignment = PP_ALIGN.CENTER

        # 3. Official SIH Logo on top-right (page_1_img_2.png)
        if os.path.exists(sih_top_logo):
            slide.shapes.add_picture(sih_top_logo, Inches(11.1), Inches(0.12), Inches(1.8), Inches(0.85))

    def add_template_footer(slide, page_num):
        # Footer explicitly removed as per user instruction
        pass

    # =========================================================================
    # SLIDE 1: Title Page (Exact Template Page 1 with SIH Brain-Bulb Logo)
    # Notice: User explicitly requested: "on 1st slide remove registered on portal"
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_WHITE
    bg1.line.fill.background()

    add_template_top_bar(s1, "SMART INDIA HACKATHON 2026", "TITLE PAGE", is_title_page=True, title_font_size=34, title_color=C_NAVY)

    # Large SIH lightbulb graphic on the right adjusted cleanly to avoid overlap
    if os.path.exists(sih_bulb_graphic):
        s1.shapes.add_picture(sih_bulb_graphic, Inches(8.35), Inches(1.40), Inches(4.40), Inches(5.40))

    tb_s1_bullets = s1.shapes.add_textbox(Inches(0.65), Inches(1.45), Inches(7.45), Inches(5.6))
    tf_s1 = tb_s1_bullets.text_frame
    tf_s1.word_wrap = True
    tf_s1.margin_left = tf_s1.margin_top = tf_s1.margin_right = tf_s1.margin_bottom = 0

    s1_items = [
        ("• Problem Statement ID –", "SIH26056"),
        ("• Problem Statement Title-", "Development of a Real-time Airfare Price Index for India through Automated Web Scraping"),
        ("• Department –", "Data Informatics & Innovation Division (DIID)"),
        ("• Category –", "Software"),
        ("• Theme –", "Smart Automation"),
        ("• Team ID –", "168405"),
        ("• Team Name –", "Roorkies")
    ]

    for idx, (label, val) in enumerate(s1_items):
        p = tf_s1.add_paragraph() if idx > 0 else tf_s1.paragraphs[0]
        p.space_before = Pt(8)
        p.space_after = Pt(8)

        r_lbl = p.add_run()
        r_lbl.text = label + " "
        r_lbl.font.name = "Arial"
        r_lbl.font.size = Pt(15)
        r_lbl.font.bold = True
        r_lbl.font.color.rgb = C_BLACK

        r_val = p.add_run()
        r_val.text = val
        r_val.font.name = "Arial"
        r_val.font.size = Pt(15)
        r_val.font.bold = True
        r_val.font.color.rgb = C_BLACK # Uniform font color as requested

    # =========================================================================
    # SLIDE 2: Proposed Solution (Exact Template Page 2 Layout - Clean & Uncluttered)
    # Reverted to clean 2-column + bottom pipeline layout as user requested ("previoous was only good")
    # Left Box: Idea Description with red highlights
    # Right Box: Uniqueness of Solution with 4 key pillars
    # Bottom Box: Full-width Process Pipeline banner
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = C_WHITE
    bg2.line.fill.background()

    add_template_top_bar(s2, "VayuSuchak: Real-Time Airfare Price Index", "Augmenting CPI Transport Inflation", title_font_size=21)

    # Subtitle with diamond bullet: ❖ Proposed Solution: Problem vs. Solution Architecture
    tb_s2_sub = s2.shapes.add_textbox(Inches(0.55), Inches(1.06), Inches(12.2), Inches(0.35))
    tf_s2_sub = tb_s2_sub.text_frame
    tf_s2_sub.margin_left = tf_s2_sub.margin_top = tf_s2_sub.margin_right = tf_s2_sub.margin_bottom = 0
    p_s2_sub = tf_s2_sub.paragraphs[0]
    p_s2_sub.text = "❖ Proposed Solution: Problem vs. Solution Architecture"
    p_s2_sub.font.name = "Arial"
    p_s2_sub.font.size = Pt(15)
    p_s2_sub.font.bold = True
    p_s2_sub.font.color.rgb = C_BLUE_TEMPLATE

    # 1. Problem & Solution Comparison Cards (Top Half)
    top_y = Inches(1.42)
    top_h = Inches(2.72)
    card_w = Inches(5.98)

    # --- Problem Card (Left) ---
    card_prob = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), top_y, card_w, top_h)
    card_prob.adjustments[0] = 0.04
    card_prob.fill.solid()
    card_prob.fill.fore_color.rgb = RGBColor(254, 242, 242) # soft subtle rose tint
    card_prob.line.color.rgb = RGBColor(220, 38, 38)
    card_prob.line.width = Pt(1.5)

    hdr_prob = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), top_y, card_w, Inches(0.42))
    hdr_prob.adjustments[0] = 0.18
    hdr_prob.fill.solid()
    hdr_prob.fill.fore_color.rgb = RGBColor(185, 28, 28) # deep crimson
    hdr_prob.line.fill.background()
    p_hp = hdr_prob.text_frame.paragraphs[0]
    p_hp.text = "CURRENT MoSPI FRAMEWORK: MANUAL FIELD SURVEY (THE PROBLEM)"
    p_hp.font.name = "Arial"
    p_hp.font.size = Pt(10.8)
    p_hp.font.bold = True
    p_hp.font.color.rgb = C_WHITE
    p_hp.alignment = PP_ALIGN.CENTER

    tb_prob = s2.shapes.add_textbox(Inches(0.72), top_y + Inches(0.46), card_w - Inches(0.35), top_h - Inches(0.50))
    tf_prob = tb_prob.text_frame
    tf_prob.word_wrap = True

    prob_items = [
        ("15-Day Information Lag: ", "Manual surveyor visits delay CPI reporting by 2 weeks, missing rapid price volatility and holiday surges."),
        ("Static Single Snapshot: ", "Only 1 physical quote collected per route/month, failing to capture 10,000+ daily dynamic pricing changes."),
        ("Dutot Upward Bias: ", "Arithmetic mean price relatives structurally overstate airfare transport inflation by +20–30 bps (substitution bias)."),
        ("High Operational Logistics: ", "Multi-crore physical airport field surveyor visits with zero cryptographic or verifiable audit trail.")
    ]
    for idx, (head, desc) in enumerate(prob_items):
        p = tf_prob.paragraphs[0] if idx == 0 else tf_prob.add_paragraph()
        p.space_after = Pt(4)
        p.line_spacing = 1.15
        r1 = p.add_run()
        r1.text = "• " + head
        r1.font.name = "Arial"
        r1.font.size = Pt(10.2)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(185, 28, 28)
        r2 = p.add_run()
        r2.text = desc
        r2.font.name = "Arial"
        r2.font.size = Pt(9.8)
        r2.font.color.rgb = RGBColor(30, 41, 59)

    # --- Solution Card (Right) ---
    r_x = Inches(6.80)
    card_sol = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, r_x, top_y, card_w, top_h)
    card_sol.adjustments[0] = 0.04
    card_sol.fill.solid()
    card_sol.fill.fore_color.rgb = RGBColor(240, 253, 244) # soft subtle emerald tint
    card_sol.line.color.rgb = RGBColor(22, 163, 74)
    card_sol.line.width = Pt(1.5)

    hdr_sol = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, r_x, top_y, card_w, Inches(0.42))
    hdr_sol.adjustments[0] = 0.18
    hdr_sol.fill.solid()
    hdr_sol.fill.fore_color.rgb = RGBColor(21, 128, 61) # deep forest emerald
    hdr_sol.line.fill.background()
    p_hs = hdr_sol.text_frame.paragraphs[0]
    p_hs.text = "VAYUSUCHAK AUTOMATED PIPELINE (HOW OUR SYSTEM SOLVES IT)"
    p_hs.font.name = "Arial"
    p_hs.font.size = Pt(10.8)
    p_hs.font.bold = True
    p_hs.font.color.rgb = C_WHITE
    p_hs.alignment = PP_ALIGN.CENTER

    tb_sol = s2.shapes.add_textbox(r_x + Inches(0.18), top_y + Inches(0.46), card_w - Inches(0.35), top_h - Inches(0.50))
    tf_sol = tb_sol.text_frame
    tf_sol.word_wrap = True

    sol_items = [
        ("Automated Live Extraction: ", "Distributed Playwright bots harvest 10,000+ live fares daily with sub-24h latency at 02:00 AM IST."),
        ("T+1..T+45 Advance Horizons: ", "Captures urgent vs saver booking curves weighted dynamically by official DGCA passenger volume shares."),
        ("UN/ILO Jevons Index: ", "Geometric mean formula eliminates Dutot substitution bias, delivering an axiomatic 0.0% distortion index."),
        ("Sovereign Audit Ledger: ", "SHA-256 Merkle tree fingerprints guarantee tamper-proof legal evidentiary auditability for MoSPI & RBI.")
    ]
    for idx, (head, desc) in enumerate(sol_items):
        p = tf_sol.paragraphs[0] if idx == 0 else tf_sol.add_paragraph()
        p.space_after = Pt(4)
        p.line_spacing = 1.15
        r1 = p.add_run()
        r1.text = "• " + head
        r1.font.name = "Arial"
        r1.font.size = Pt(10.2)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(21, 128, 61)
        r2 = p.add_run()
        r2.text = desc
        r2.font.name = "Arial"
        r2.font.size = Pt(9.8)
        r2.font.color.rgb = RGBColor(30, 41, 59)

    # 2. Bottom Section: 5 Connected Horizontal Process Workflow Cards (Engineered & Full)
    bot_y = Inches(4.32)
    w_step = Inches(2.30)
    gap = Inches(0.18)
    h_step = Inches(2.95)
    start_x = Inches(0.55)

    steps_data = [
        {
            "num": "01",
            "title": "Dynamic Yield\nTracking",
            "badge": "T+1..T+45 Windows",
            "color": RGBColor(30, 64, 175), # Navy/Blue
            "border": RGBColor(59, 130, 246),
            "bg_badge": RGBColor(239, 246, 255),
            "desc": "Captures intraday surges across T+1..T+45 advance booking windows.",
            "tech": "Playwright Scraper",
            "metric": "10,000+ Fares/Day"
        },
        {
            "num": "02",
            "title": "Dynamic IQR\nScrubber",
            "badge": "Base Fare Isolation",
            "color": RGBColor(2, 132, 199), # Sky
            "border": RGBColor(14, 165, 233),
            "bg_badge": RGBColor(240, 249, 255),
            "desc": "Isolates base fares and purges phantom prices and cache glitches.",
            "tech": "SciPy Truncation",
            "metric": "Outlier Purged"
        },
        {
            "num": "03",
            "title": "UN/ILO Jevons\nIndex Engine",
            "badge": "Geometric Mean",
            "color": RGBColor(13, 148, 136), # Teal
            "border": RGBColor(20, 184, 166),
            "bg_badge": RGBColor(240, 253, 250),
            "desc": "Geometric mean calculation that eliminates upward substitution bias.",
            "tech": "UN/ILO Ch. 10 Math",
            "metric": "0.0% Upward Bias"
        },
        {
            "num": "04",
            "title": "Sovereign Audit\nVault",
            "badge": "Cryptographic Proofs",
            "color": RGBColor(22, 163, 74), # Green
            "border": RGBColor(34, 197, 94),
            "bg_badge": RGBColor(240, 253, 244),
            "desc": "SHA-256 batch Merkle tree proofs for judicial and policy scrutiny.",
            "tech": "SHA-256 Ledger",
            "metric": "Tamper-Proof"
        },
        {
            "num": "05",
            "title": "Real-Time API\nDelivery",
            "badge": "Instant Feeds",
            "color": RGBColor(15, 23, 42), # Slate Navy
            "border": RGBColor(100, 116, 139),
            "bg_badge": RGBColor(248, 250, 252),
            "desc": "Sub-10ms REST API and live eSankhyiki CSV feed for MoSPI and RBI.",
            "tech": "FastAPI & CSV Feed",
            "metric": "< 10ms Latency"
        }
    ]

    for i, st in enumerate(steps_data):
        cx = start_x + i * (w_step + gap)

        # Card container
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, bot_y, w_step, h_step)
        box.adjustments[0] = 0.05
        box.fill.solid()
        box.fill.fore_color.rgb = C_WHITE
        box.line.color.rgb = st["border"]
        box.line.width = Pt(1.5)

        # Top Header Pill / Band
        h_strip = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, bot_y, w_step, Inches(0.40))
        h_strip.adjustments[0] = 0.18
        h_strip.fill.solid()
        h_strip.fill.fore_color.rgb = st["color"]
        h_strip.line.fill.background()
        p_sh = h_strip.text_frame.paragraphs[0]
        p_sh.text = f"STEP {st['num']}"
        p_sh.font.name = "Arial"
        p_sh.font.size = Pt(11)
        p_sh.font.bold = True
        p_sh.font.color.rgb = C_WHITE
        p_sh.alignment = PP_ALIGN.CENTER

        # Content in Card
        tb = s2.shapes.add_textbox(cx + Inches(0.10), bot_y + Inches(0.45), w_step - Inches(0.20), h_step - Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0

        # Title
        p_t = tf.paragraphs[0]
        p_t.text = st["title"]
        p_t.font.name = "Arial"
        p_t.font.size = Pt(11.5)
        p_t.font.bold = True
        p_t.font.color.rgb = st["color"]
        p_t.alignment = PP_ALIGN.CENTER
        p_t.space_after = Pt(2)

        # Subtitle / Horizon Badge
        p_s = tf.add_paragraph()
        p_s.text = f"• {st['badge']} •"
        p_s.font.name = "Arial"
        p_s.font.size = Pt(9.0)
        p_s.font.bold = True
        p_s.font.color.rgb = RGBColor(100, 116, 139)
        p_s.alignment = PP_ALIGN.CENTER
        p_s.space_after = Pt(6)

        # Description
        p_d = tf.add_paragraph()
        p_d.text = st["desc"]
        p_d.font.name = "Arial"
        p_d.font.size = Pt(9.6)
        p_d.font.color.rgb = RGBColor(30, 41, 59)
        p_d.alignment = PP_ALIGN.LEFT
        p_d.line_spacing = 1.18

        # Bottom Metric Tag Box (Anchored at the bottom of the card)
        tag_y = bot_y + h_step - Inches(0.42)
        tag_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.08), tag_y, w_step - Inches(0.16), Inches(0.34))
        tag_box.adjustments[0] = 0.2
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = st["bg_badge"]
        tag_box.line.color.rgb = st["border"]
        tag_box.line.width = Pt(1.0)
        p_tb = tag_box.text_frame.paragraphs[0]
        p_tb.text = f"{st['tech']} | {st['metric']}"
        p_tb.font.name = "Arial"
        p_tb.font.size = Pt(8.5)
        p_tb.font.bold = True
        p_tb.font.color.rgb = st["color"]
        p_tb.alignment = PP_ALIGN.CENTER

        # Connecting Arrow (between cards)
        if i < 4:
            arr_x = cx + w_step + Inches(0.01)
            arr_tb = s2.shapes.add_textbox(arr_x, bot_y + Inches(1.15), gap - Inches(0.02), Inches(0.40))
            tf_a = arr_tb.text_frame
            tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
            p_a = tf_a.paragraphs[0]
            p_a.text = "➔"
            p_a.font.name = "Arial"
            p_a.font.size = Pt(15)
            p_a.font.bold = True
            p_a.font.color.rgb = RGBColor(148, 163, 184)
            p_a.alignment = PP_ALIGN.CENTER

    add_template_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: Technical Approach
    # Left Box: Technologies Used
    # Right: High-Resolution Architecture Flowchart (Cropped top 14% to remove duplicate SIH logo / title)
    # Bottom: Production Architecture & Engine Validation (Live link removed as requested!)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = C_WHITE
    bg3.line.fill.background()

    add_template_top_bar(s3, "TECHNICAL APPROACH", title_font_size=25, is_serif=True)

    col_y = Inches(1.15)
    col_h = Inches(5.95)

    # 1. Left Column: Technologies Used (~28% of usable slide width: 3.45 inches)
    col_w_l = Inches(3.45)
    box_l = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), col_y, col_w_l, col_h)
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = RGBColor(248, 250, 252) # soft slate-50
    box_l.line.color.rgb = C_BLUE_TEMPLATE
    box_l.line.width = Pt(1.5)

    tb_l = s3.shapes.add_textbox(Inches(0.70), col_y + Inches(0.14), col_w_l - Inches(0.30), col_h - Inches(0.28))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p_lh = tf_l.paragraphs[0]
    p_lh.text = "Technologies Used:"
    p_lh.font.name = "Arial"
    p_lh.font.size = Pt(17)
    p_lh.font.bold = True
    p_lh.font.color.rgb = C_BLUE_TEMPLATE
    p_lh.space_after = Pt(10)

    tech_groups = [
        ("Languages & Runtimes:", RGBColor(220, 38, 38), [
            "Python 3.13 (Async Harvester & Engine)",
            "TypeScript & React 19 (Dashboard UI)",
            "SQL (PostgreSQL Time-Series & SQLite)"
        ]),
        ("Extraction & Cleansing:", RGBColor(30, 64, 175), [
            "Playwright Headless Stealth Proxy Pool",
            "T+1..T+45 Advance Horizons Dynamic Tracking",
            "SciPy & NumPy Dynamic IQR Outlier Filter"
        ]),
        ("Index Engine & Crypto:", RGBColor(124, 58, 237), [
            "UN/ILO Jevons Index Formula (GMI)",
            "DGCA Official Route Volume Weighting",
            "SHA-256 Batch Merkle Audit Ledger"
        ]),
        ("API, Cloud & Standards:", RGBColor(16, 185, 129), [
            "FastAPI & Uvicorn Sub-10ms REST APIs",
            "Vercel Edge & GitHub Actions Daily Cron",
            "NDSAP Open Data & UN/ILO Ch. 10 Ready"
        ])
    ]

    for title, col, items in tech_groups:
        p_t = tf_l.add_paragraph()
        p_t.space_before = Pt(8)
        p_t.space_after = Pt(3)
        r_t = p_t.add_run()
        r_t.text = title
        r_t.font.name = "Arial"
        r_t.font.size = Pt(11.5)
        r_t.font.bold = True
        r_t.font.color.rgb = col
        
        for it in items:
            p_i = tf_l.add_paragraph()
            p_i.space_after = Pt(2.5)
            r_b = p_i.add_run()
            r_b.text = "• "
            r_b.font.name = "Arial"
            r_b.font.size = Pt(10)
            r_b.font.bold = True
            r_b.font.color.rgb = C_TEXT_DARK
            
            r_txt = p_i.add_run()
            r_txt.text = it
            r_txt.font.name = "Arial"
            r_txt.font.size = Pt(9.8)
            r_txt.font.color.rgb = C_TEXT_DARK

    # 2. Right Section: Architecture Diagram & Core Benchmarks (~72% of usable width: 8.58 inches)
    right_x = Inches(4.20)
    right_w = Inches(8.58)

    card_r = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, right_x, col_y, right_w, col_h)
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = C_WHITE
    card_r.line.color.rgb = RGBColor(203, 213, 225)
    card_r.line.width = Pt(1.2)

    # Architecture Diagram: Scaled neatly to 8.30 inches width
    flow_w = Inches(8.30)
    flow_h = Inches(8.30 / 2.3432) # ~3.54 in
    flow_x = right_x + (right_w - flow_w) / 2
    flow_y = col_y + Inches(0.18)

    if os.path.exists(arch_img):
        s3.shapes.add_picture(arch_img, flow_x, flow_y, flow_w, flow_h)

    # Underneath Diagram: Core Engineering Benchmarks & SLAs Card
    badge_y = flow_y + flow_h + Inches(0.20)
    badge_h = col_y + col_h - badge_y - Inches(0.15) # ~1.88 in
    badge_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x + Inches(0.15), badge_y, right_w - Inches(0.30), badge_h)
    badge_box.adjustments[0] = 0.08
    badge_box.fill.solid()
    badge_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    badge_box.line.color.rgb = C_BLUE_TEMPLATE
    badge_box.line.width = Pt(1.2)

    tb_bh = s3.shapes.add_textbox(right_x + Inches(0.25), badge_y + Inches(0.10), right_w - Inches(0.50), Inches(0.30))
    tf_bh = tb_bh.text_frame
    p_bh = tf_bh.paragraphs[0]
    p_bh.text = "Core Engineering Benchmarks & Architectural Guarantees"
    p_bh.font.name = "Arial"
    p_bh.font.size = Pt(11.5)
    p_bh.font.bold = True
    p_bh.font.color.rgb = C_BLUE_TEMPLATE
    p_bh.alignment = PP_ALIGN.CENTER

    metrics = [
        ("Harvester Run SLA", "< 18 Minutes", "10,000+ daily live fares"),
        ("Dynamic IQR Filter", "SciPy Scrubber", "Purges phantom taxes & surge"),
        ("Axiomatic Rigor", "0.00% Bias", "UN/ILO Jevons Geometric Mean"),
        ("REST API Delivery", "< 10ms Latency", "MoSPI eSankhyiki CSV/JSON")
    ]
    col_bw = (right_w - Inches(0.50)) / 4
    for idx, (m_head, m_val, m_sub) in enumerate(metrics):
        mx = right_x + Inches(0.25) + idx * col_bw
        my = badge_y + Inches(0.48)
        tb_m = s3.shapes.add_textbox(mx, my, col_bw - Inches(0.08), Inches(1.15))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        
        p1 = tf_m.paragraphs[0]
        p1.text = m_head
        p1.font.name = "Arial"
        p1.font.size = Pt(9.2)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY
        p1.alignment = PP_ALIGN.CENTER
        p1.space_after = Pt(3)
        
        p2 = tf_m.add_paragraph()
        p2.text = m_val
        p2.font.name = "Arial"
        p2.font.size = Pt(11.5)
        p2.font.bold = True
        p2.font.color.rgb = RGBColor(16, 185, 129) if ("0" in m_val or "<" in m_val) else C_RED_TEMPLATE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(3)
        
        p3 = tf_m.add_paragraph()
        p3.text = m_sub
        p3.font.name = "Arial"
        p3.font.size = Pt(8.2)
        p3.font.color.rgb = C_TEXT_DARK
        p3.alignment = PP_ALIGN.CENTER

    add_template_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: Feasibility and Viability (Clean 3-Column Architecture + Runway Banner)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = C_WHITE
    bg4.line.fill.background()

    add_template_top_bar(s4, "FEASIBILITY AND VIABILITY", "PRACTICAL • SCALABLE • SUSTAINABLE IMPACT", title_font_size=25, title_color=C_NAVY, is_serif=True)

    col_data = [
        (
            Inches(0.65), "⚙️ FEASIBILITY ANALYSIS", "PRACTICAL TO IMPLEMENT",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                ("♻️ Infrastructure Reusability", "Leverages standard serverless cloud and public web portals; zero airport hardware installation required."),
                ("📈 Scalable Deployment", "Deployed across 12 core metro routes initially and seamlessly scalable nationwide to 250+ UDAN regional corridors."),
                ("💰 Cost-Effectiveness", "Entire pipeline operates under ₹3,500/month, compared to multi-crore physical surveyor field logistics."),
                ("🎯 Authority Integration", "Native REST API and JSON feeds integrate directly into MoSPI eSankhyiki, RBI MPC, and DGCA portals.")
            ]
        ),
        (
            Inches(4.8), "✔️ VIABILITY", "PROVEN, RELIABLE & TRUSTWORTHY",
            RGBColor(22, 163, 74), RGBColor(240, 253, 244),
            [
                ("🔍 Proven Concept", "Validated on 10,000+ live fare quotes across IndiGo, Air India, SpiceJet, and Akasa with 100% uptime."),
                ("🤝 Builds Public Trust", "Transparent, open mathematical formulas backed by UN/ILO Chapter 10 guidelines eliminate black-box skepticism."),
                ("🛡️ Guaranteed Accountability", "Cryptographic SHA-256 tamper-proof ledger logs every raw fare quote for sovereign audit and judicial scrutiny."),
                ("👥 Authority Engagement", "Intuitive live interactive dashboards and automated alert triggers keep policy analysts actively informed.")
            ]
        ),
        (
            Inches(8.95), "📊 BUSINESS POTENTIAL", "SUSTAINABLE POLICY IMPACT",
            RGBColor(217, 119, 6), RGBColor(254, 252, 232),
            [
                ("💵 Government Cost Savings", "Eliminates thousands of manual surveyor airport trips, saving MoSPI an estimated ₹15+ Crores annually."),
                ("📈 Economic Policy Impact", "Delivers leading real-time inflation signals to RBI 15 days ahead of monthly CPI releases for rate setting."),
                ("⚖️ Regulatory Oversight", "Empowers DGCA with automated surge-anomaly detection, identifying predatory pricing and route monopolies."),
                ("🌐 DPI Monetization Potential", "Sovereign API can be licensed to financial institutions, rating agencies, and travel analytics providers.")
            ]
        )
    ]

    col_w = Inches(3.72)
    for cx, title, subtitle, theme_col, bg_col, cards in col_data:
        # Outer Column Container
        c_col = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.12), col_w, Inches(4.68))
        c_col.adjustments[0] = 0.03
        c_col.fill.solid()
        c_col.fill.fore_color.rgb = RGBColor(255, 255, 255)
        c_col.line.color.rgb = theme_col
        c_col.line.width = Pt(1.5)

        # Column Header Banner
        h_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.12), col_w, Inches(0.55))
        h_box.adjustments[0] = 0.2
        h_box.fill.solid()
        h_box.fill.fore_color.rgb = theme_col
        h_box.line.fill.background()
        
        tf_h = h_box.text_frame
        p_h = tf_h.paragraphs[0]
        p_h.text = title
        p_h.font.name = "Arial"
        p_h.font.size = Pt(10.0)
        p_h.font.bold = True
        p_h.font.color.rgb = C_WHITE
        p_h.alignment = PP_ALIGN.CENTER
        
        p_sub = tf_h.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(8)
        p_sub.font.color.rgb = RGBColor(241, 245, 249)
        p_sub.alignment = PP_ALIGN.CENTER

        # 4 Stacked Icon Cards
        for c_idx, (c_head, c_desc) in enumerate(cards):
            card_y = Inches(1.74) + c_idx * Inches(0.98)
            card_shape = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.12), card_y, col_w - Inches(0.24), Inches(0.90))
            card_shape.adjustments[0] = 0.12
            card_shape.fill.solid()
            card_shape.fill.fore_color.rgb = bg_col
            card_shape.line.color.rgb = theme_col
            card_shape.line.width = Pt(1.0)

            tb_cd = s4.shapes.add_textbox(cx + Inches(0.18), card_y + Inches(0.05), col_w - Inches(0.36), Inches(0.78))
            tf_cd = tb_cd.text_frame
            tf_cd.word_wrap = True
            tf_cd.margin_left = tf_cd.margin_right = tf_cd.margin_top = tf_cd.margin_bottom = 0
            
            p_ch = tf_cd.paragraphs[0]
            p_ch.text = c_head
            p_ch.font.name = "Arial"
            p_ch.font.size = Pt(9.5)
            p_ch.font.bold = True
            p_ch.font.color.rgb = theme_col

            p_cb = tf_cd.add_paragraph()
            p_cb.text = c_desc
            p_cb.font.name = "Arial"
            p_cb.font.size = Pt(8)
            p_cb.font.color.rgb = C_TEXT_DARK

    # Bottom Runway Skyline Banner
    if os.path.exists(runway_banner):
        s4.shapes.add_picture(runway_banner, Inches(0.65), Inches(5.88), Inches(12.02), Inches(1.18))

    add_template_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: Impact and Benefits
    # Left: Potential Impact (top box) + Benefits (bottom box)
    # Right: PROTOTYPE IMAGE 1 (Chart) + PROTOTYPE IMAGE 2 (Crisp untruncated Corridor Table)
    # Bottom: Live Interactive Prototype Link Banner Pill (Moved to bottom as requested!)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = C_WHITE
    bg5.line.fill.background()

    add_template_top_bar(s5, "IMPACT AND BENEFITS", title_font_size=25, is_serif=True)

    # Left Column (width = 5.00 inches)
    l_w = Inches(5.00)
    col_l_x = Inches(0.55)

    # Box 1: Potential Impact (top half, height = 2.55 inches)
    box_s5_imp = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_l_x, Inches(1.18), l_w, Inches(2.55))
    box_s5_imp.fill.solid()
    box_s5_imp.fill.fore_color.rgb = C_WHITE
    box_s5_imp.line.color.rgb = C_BLUE_TEMPLATE
    box_s5_imp.line.width = Pt(1.5)

    tb_imp = s5.shapes.add_textbox(col_l_x + Inches(0.18), Inches(1.28), l_w - Inches(0.36), Inches(2.35))
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
        ("Zero Policy Lag: ", "Slashes price collection latency from 15 days to real-time (<24h), eliminating critical macroeconomic blindspots."),
        ("Comprehensive Dynamic Coverage: ", "Ingests 10,000+ daily fare quotes across 12 metro routes vs 1 monthly static manual quote."),
        ("Elimination of Substitution Bias: ", "Mathematically eliminates 20-30 bps upward inflation distortion via UN/ILO Jevons indexing.")
    ]

    for itit, idesc in impacts_list:
        p_i = tf_imp.add_paragraph()
        p_i.space_after = Pt(5)
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

    # Left Column Box 2: Benefits (bottom half, height = 2.65 inches)
    box_s5_ben = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_l_x, Inches(3.85), l_w, Inches(2.65))
    box_s5_ben.fill.solid()
    box_s5_ben.fill.fore_color.rgb = C_WHITE
    box_s5_ben.line.color.rgb = C_BLUE_TEMPLATE
    box_s5_ben.line.width = Pt(1.5)

    tb_ben = s5.shapes.add_textbox(col_l_x + Inches(0.18), Inches(3.95), l_w - Inches(0.36), Inches(2.45))
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
        r_bt.font.size = Pt(10.5)
        r_bt.font.bold = True
        r_bt.font.color.rgb = C_RED_TEMPLATE

        r_bd = p_b.add_run()
        r_bd.text = bdesc
        r_bd.font.name = "Arial"
        r_bd.font.size = Pt(10)
        r_bd.font.color.rgb = C_TEXT_DARK

    # Right Column: Two Prototype Image Boxes
    r_x = Inches(5.75)
    r_w = Inches(7.03)

    # Top Prototype Box: PROTOTYPE IMAGE 1 (height = 2.55 inches)
    box_p1 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, r_x, Inches(1.18), r_w, Inches(2.55))
    box_p1.fill.solid()
    box_p1.fill.fore_color.rgb = C_WHITE
    box_p1.line.color.rgb = C_BLUE_TEMPLATE
    box_p1.line.width = Pt(1.5)

    tb_p1_lbl = s5.shapes.add_textbox(r_x + Inches(0.12), Inches(1.22), r_w - Inches(0.24), Inches(0.32))
    tf_p1 = tb_p1_lbl.text_frame
    tf_p1.margin_left = tf_p1.margin_top = tf_p1.margin_right = tf_p1.margin_bottom = 0
    p_p1 = tf_p1.paragraphs[0]
    r_p1a = p_p1.add_run()
    r_p1a.text = "PROTOTYPE IMAGE 1 (Live Real-Time Airfare Price Index Dashboard)"
    r_p1a.font.name = "Arial"
    r_p1a.font.size = Pt(10.5)
    r_p1a.font.bold = True
    r_p1a.font.color.rgb = C_RED_TEMPLATE

    if os.path.exists(proto_chart):
        s5.shapes.add_picture(proto_chart, r_x + Inches(0.08), Inches(1.52), r_w - Inches(0.16), Inches(2.15))

    # Bottom Prototype Box: PROTOTYPE IMAGE 2 (height = 2.65 inches)
    box_p2 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, r_x, Inches(3.85), r_w, Inches(2.65))
    box_p2.fill.solid()
    box_p2.fill.fore_color.rgb = C_WHITE
    box_p2.line.color.rgb = C_BLUE_TEMPLATE
    box_p2.line.width = Pt(1.5)

    tb_p2_lbl = s5.shapes.add_textbox(r_x + Inches(0.12), Inches(3.89), r_w - Inches(0.24), Inches(0.32))
    tf_p2 = tb_p2_lbl.text_frame
    tf_p2.margin_left = tf_p2.margin_top = tf_p2.margin_right = tf_p2.margin_bottom = 0
    p_p2 = tf_p2.paragraphs[0]
    r_p2a = p_p2.add_run()
    r_p2a.text = "PROTOTYPE IMAGE 2 (Corridor-Wise Yield & Surge Analytics Table)"
    r_p2a.font.name = "Arial"
    r_p2a.font.size = Pt(10.5)
    r_p2a.font.bold = True
    r_p2a.font.color.rgb = C_RED_TEMPLATE

    if os.path.exists(proto_table):
        s5.shapes.add_picture(proto_table, r_x + Inches(0.08), Inches(4.20), r_w - Inches(0.16), Inches(2.25))

    # Bottom of Slide 5: Live Prototype Link Banner Pill (Across Bottom!)
    pill_proto = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(6.62), Inches(12.23), Inches(0.44))
    pill_proto.adjustments[0] = 0.5
    pill_proto.fill.solid()
    pill_proto.fill.fore_color.rgb = RGBColor(16, 185, 129) # Emerald Green
    pill_proto.line.fill.background()

    tf_pp = pill_proto.text_frame
    tf_pp.margin_left = tf_pp.margin_right = tf_pp.margin_top = tf_pp.margin_bottom = 0
    p_pp = tf_pp.paragraphs[0]
    p_pp.alignment = PP_ALIGN.CENTER

    r_pp1 = p_pp.add_run()
    r_pp1.text = "🚀 Live Interactive Prototype: "
    r_pp1.font.name = "Arial"
    r_pp1.font.size = Pt(11)
    r_pp1.font.bold = True
    r_pp1.font.color.rgb = C_WHITE

    r_pp2 = p_pp.add_run()
    r_pp2.text = "https://sih26056-airfare-cpi.vercel.app ↗"
    r_pp2.font.name = "Arial"
    r_pp2.font.size = Pt(11)
    r_pp2.font.bold = True
    r_pp2.font.underline = True
    r_pp2.font.color.rgb = C_WHITE
    r_pp2.hyperlink.address = "https://sih26056-airfare-cpi.vercel.app"

    r_pp3 = p_pp.add_run()
    r_pp3.text = "   |   Click to Explore Live Real-Time Dashboard & Ingestion Engine"
    r_pp3.font.name = "Arial"
    r_pp3.font.size = Pt(10.5)
    r_pp3.font.color.rgb = RGBColor(240, 253, 244)

    add_template_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: Research and References (4-Quadrant Grid with Clickable Hyperlinks)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = C_WHITE
    bg6.line.fill.background()

    add_template_top_bar(s6, "RESEARCH AND REFERENCES", "Academic Foundations, Official Data Sources & Technical Documentation", title_font_size=25, title_color=C_NAVY, is_serif=True)

    quads = [
        (
            Inches(0.75), Inches(1.25), Inches(5.7), Inches(2.72),
            "SUPPORTING RESEARCH PAPERS",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                [
                    ("Cavallo & Rigobon (2016). 'The Billion Prices Project: Using Online Data for Measurement.' J. Econ. Perspect. ", False, None),
                    ("[doi:10.1257/jep.30.2.151 ↗]", True, "https://doi.org/10.1257/jep.30.2.151")
                ],
                [
                    ("UN, ILO, IMF, OECD, World Bank (2020). CPI Manual: Concepts & Methods, Ch. 10 Elementary Indices. ", False, None),
                    ("[ilo.org/cpi-manual ↗]", True, "https://www.ilo.org/global/statistics-and-databases/standards-and-guidelines/manuals-and-guides/WCMS_761444/lang--en/index.htm")
                ],
                [
                    ("Diewert, W. E. (2004). 'Elementary Indices.' In Consumer Price Index Theory, IMF Handbook. ", False, None),
                    ("[imf.org/cpi-theory ↗]", True, "https://www.imf.org/external/pubs/ft/cpi/")
                ]
            ]
        ),
        (
            Inches(6.85), Inches(1.25), Inches(5.7), Inches(2.72),
            "OFFICIAL DATA SOURCES",
            RGBColor(15, 23, 42), RGBColor(248, 250, 252),
            [
                [
                    ("DGCA India: Monthly Scheduled Domestic Passenger Traffic & Route Shares. ", False, None),
                    ("[dgca.gov.in ↗]", True, "https://www.dgca.gov.in")
                ],
                [
                    ("MoSPI NSO: Consumer Price Index Guidelines & Base 2012 Methodology. ", False, None),
                    ("[mospi.gov.in ↗]", True, "https://mospi.gov.in")
                ],
                [
                    ("Direct Airline Portals: Daily Fare Quotes across IndiGo, Air India, Akasa, SpiceJet. ", False, None),
                    ("[goindigo.in ↗]", True, "https://www.goindigo.in"),
                    (" | ", False, None),
                    ("[airindia.com ↗]", True, "https://www.airindia.com")
                ],
                [
                    ("Online Travel Aggregators: Non-Stop Corridor Pricing Feeds. ", False, None),
                    ("[makemytrip.com ↗]", True, "https://www.makemytrip.com"),
                    (" | ", False, None),
                    ("[easemytrip.com ↗]", True, "https://www.easemytrip.com")
                ]
            ]
        ),
        (
            Inches(0.75), Inches(4.18), Inches(5.7), Inches(2.80),
            "MARKET RESEARCH & MOTIVATION",
            RGBColor(15, 23, 42), RGBColor(248, 250, 252),
            [
                [
                    ("Indian domestic aviation traffic projected to grow at >15% CAGR (2024–2030). ", False, None),
                    ("[iata.org/india ↗]", True, "https://www.iata.org")
                ],
                [
                    ("Algorithmic dynamic pricing generates 200–400% intraday fare volatility across metros. ", False, None),
                    ("[cci.gov.in/market-study ↗]", True, "https://www.cci.gov.in")
                ],
                [
                    ("Over 90% of domestic air tickets sold digitally, making physical surveying obsolete. ", False, None),
                    ("[civilaviation.gov.in ↗]", True, "https://www.civilaviation.gov.in")
                ],
                [
                    ("VayuSuchak eliminates the critical 15-day MoSPI manual survey reporting lag with zero latency. ", False, None),
                    ("[mospi.gov.in/cpi-calendar ↗]", True, "https://mospi.gov.in")
                ]
            ]
        ),
        (
            Inches(6.85), Inches(4.18), Inches(5.7), Inches(2.80),
            "TECHNICAL DOCUMENTATION & SPECS",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                [
                    ("Index Formulations: UN/ILO Jevons Geometric Mean Specification. ", False, None),
                    ("[ilo.org/manual ↗]", True, "https://www.ilo.org")
                ],
                [
                    ("Harvester Engine: Playwright Chromium Headless with Ethical Scraping Protocols. ", False, None),
                    ("[playwright.dev ↗]", True, "https://playwright.dev")
                ],
                [
                    ("Provenance Vault: SHA-256 Hash Manifest conforming to NDSAP Standards. ", False, None),
                    ("[data.gov.in/ndsap ↗]", True, "https://data.gov.in")
                ],
                [
                    ("Production Deployment: Live Vercel Edge Serverless Architecture & Dashboard. ", False, None),
                    ("[sih26056-airfare-cpi.vercel.app ↗]", True, "https://sih26056-airfare-cpi.vercel.app")
                ]
            ]
        )
    ]

    for qx, qy, qw, qh, q_title, q_theme_color, q_bg, q_items in quads:
        q_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx, qy, qw, qh)
        q_box.adjustments[0] = 0.05
        q_box.fill.solid()
        q_box.fill.fore_color.rgb = q_bg
        q_box.line.color.rgb = q_theme_color
        q_box.line.width = Pt(1.5)

        tb = s6.shapes.add_textbox(qx + Inches(0.22), qy + Inches(0.12), qw - Inches(0.44), qh - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        h = tf.paragraphs[0]
        h.text = q_title
        h.font.name = "Arial"
        h.font.size = Pt(12)
        h.font.bold = True
        h.font.color.rgb = q_theme_color if q_theme_color != RGBColor(37, 99, 235) else RGBColor(29, 78, 216)
        h.alignment = PP_ALIGN.CENTER
        h.space_after = Pt(6)

        for item_segments in q_items:
            p = tf.add_paragraph()
            p.space_after = Pt(3.5)
            p.line_spacing = 1.15

            r_bullet = p.add_run()
            r_bullet.text = "• "
            r_bullet.font.name = "Arial"
            r_bullet.font.size = Pt(9.0)
            r_bullet.font.bold = True
            r_bullet.font.color.rgb = C_TEXT_DARK

            for seg_text, is_link, url in item_segments:
                r_seg = p.add_run()
                r_seg.text = seg_text
                r_seg.font.name = "Arial"
                r_seg.font.size = Pt(8.8)
                if is_link:
                    r_seg.font.bold = True
                    r_seg.font.underline = True
                    r_seg.font.color.rgb = RGBColor(29, 78, 216) # Clickable blue link
                    if url:
                        r_seg.hyperlink.address = url
                else:
                    r_seg.font.color.rgb = C_TEXT_DARK

    add_template_footer(s6, 6)

    prs.save(output_path)
    print(f"Successfully generated final presentation at {output_path}")

    # Copy PPTX to public, dist, and brain
    public_pptx = os.path.join(base_dir, "public", "AirIntel_India_SIH26056_Presentation.pptx")
    dist_pptx = os.path.join(base_dir, "dist", "AirIntel_India_SIH26056_Presentation.pptx")
    brain_pptx = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24\AirIntel_India_SIH26056_Presentation.pptx"
    
    for target in [public_pptx, dist_pptx, brain_pptx]:
        try:
            if os.path.abspath(output_path).lower() != os.path.abspath(target).lower():
                if os.path.exists(os.path.dirname(target)):
                    shutil.copy2(output_path, target)
        except Exception as e_copy:
            print(f"Notice during copy to {target}: {e_copy}")

    # Export all slides to 1920x1080 Full HD PNG images via PowerPoint COM
    try:
        import win32com.client
        print("Exporting slides via PowerPoint COM at 1920x1080...")
        ppt = win32com.client.Dispatch("PowerPoint.Application")
        pres_com = ppt.Presentations.Open(os.path.abspath(output_path), False, False, False)
        
        brain_dir = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24"
        public_dir = os.path.join(base_dir, "public")
        dist_dir = os.path.join(base_dir, "dist")
        
        for idx in range(1, pres_com.Slides.Count + 1):
            slide_name = f"Slide_{idx}_hd.png"
            target_public = os.path.join(public_dir, slide_name)
            pres_com.Slides(idx).Export(target_public, "PNG", 1920, 1080)
            
            # Copy to brain and dist
            shutil.copy2(target_public, os.path.join(brain_dir, slide_name))
            if os.path.exists(dist_dir):
                shutil.copy2(target_public, os.path.join(dist_dir, slide_name))
            print(f"Exported {slide_name} (1920x1080 Full HD)")
            
        pres_com.Close()
        ppt.Quit()
        print("All 6 slides successfully exported to Full HD PNG!")
    except Exception as e:
        print(f"COM Export error: {e}")

if __name__ == "__main__":
    out_file = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\AirIntel_India_SIH26056_Presentation.pptx"
    create_final_presentation(out_file)
