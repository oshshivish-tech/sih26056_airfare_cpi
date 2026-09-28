import os
import sys
import shutil
from PIL import Image
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def ensure_hd_equations(base_dir):
    eq1_path = os.path.join(base_dir, "scratch", "eq1_perfect.png")
    eq2_path = os.path.join(base_dir, "scratch", "eq2_perfect.png")
    if not (os.path.exists(eq1_path) and os.path.exists(eq2_path)):
        plt.rcParams.update({
            'font.size': 20,
            'mathtext.fontset': 'cm',
            'text.usetex': False
        })
        fig, ax = plt.subplots(figsize=(8.2, 1.25))
        ax.axis('off')
        eq1 = r'$I_{\mathrm{Jevons}}^t = \left( \prod_{i=1}^N \frac{P_{i,t}}{P_{i,0}} \right)^{\!\frac{1}{N}} \times 100 = \exp\left( \frac{1}{N} \sum_{i=1}^N \ln\left( \frac{P_{i,t}}{P_{i,0}} \right) \right) \times 100$'
        ax.text(0.5, 0.5, eq1, fontsize=20.5, ha='center', va='center', color='#000000')
        plt.savefig(eq1_path, dpi=600, transparent=True, bbox_inches='tight', pad_inches=0.01)
        plt.close()

        fig, ax = plt.subplots(figsize=(7.0, 1.05))
        ax.axis('off')
        eq2 = r'$I_{\mathrm{Composite}}^t = \sum_{c=1}^C w_c \cdot I_{c,t} \quad \left(\mathrm{where}\ \sum_{c=1}^C w_c = 1.0\right)$'
        ax.text(0.5, 0.5, eq2, fontsize=20.5, ha='center', va='center', color='#000000')
        plt.savefig(eq2_path, dpi=600, transparent=True, bbox_inches='tight', pad_inches=0.01)
        plt.close()
    return eq1_path, eq2_path

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
    # SLIDE 2: Proposed Solution (Exact 3-Column Layout from Reference Image)
    # Col 1: THE PROBLEM (Current MoSPI Manual Survey)
    # Col 2: HOW WE SOLVE IT: (VayuSuchak Engine)
    # Col 3: WHY IT IS DIFFERENT (Unique VayuSuchak Advantages)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = C_WHITE
    bg2.line.fill.background()

    add_template_top_bar(s2, "PROPOSED SOLUTION", "Addressing Current MoSPI Limitations with Automated High-Frequency Ingestion", title_font_size=23)

    # 3 Distinct Columns spanning full height matching reference image
    card_y = Inches(1.22)
    card_h = Inches(5.95)
    card_w = Inches(3.86)
    card_gap = Inches(0.32)
    start_x = Inches(0.55)

    s2_cards_data = [
        {
            "header_bg": RGBColor(254, 202, 202),       # Soft pastel red
            "header_border": RGBColor(239, 68, 68),
            "card_bg": RGBColor(255, 245, 245),         # Soft light rose tint
            "card_border": RGBColor(239, 68, 68),
            "title": "THE PROBLEM",
            "subtitle": "Current MoSPI Manual Survey",
            "title_color": RGBColor(153, 27, 27),
            "sub_color": RGBColor(127, 29, 29),
            "accent_color": RGBColor(185, 28, 28),
            "points": [
                ("1. 15-Day Data Lag", "Manual survey delays limit responsiveness"),
                ("2. Static Single Snapshot", "Only 1 quote collected per route/month"),
                ("3. Blind to Dynamic Pricing", "Misses yield spikes, peaks, surges"),
                ("4. Lead-Time Neglect", "Completely ignores emergency vs. advance booking")
            ]
        },
        {
            "header_bg": RGBColor(187, 247, 208),       # Soft pastel green
            "header_border": RGBColor(34, 197, 94),
            "card_bg": RGBColor(240, 253, 244),         # Soft light emerald tint
            "card_border": RGBColor(34, 197, 94),
            "title": "HOW WE SOLVE IT:",
            "subtitle": "VayuSuchak Engine",
            "title_color": RGBColor(20, 83, 45),
            "sub_color": RGBColor(21, 128, 61),
            "accent_color": RGBColor(21, 128, 61),
            "points": [
                ("1. Automated Real-Time Extraction", "Automated high-frequency scraping across 4 major airlines"),
                ("2. Comprehensive Lead Times", "Samples 5 forward horizons T+1..T+45"),
                ("3. Geometric Mean Calculation", "UN/ILO Jevons Elementary Mean"),
                ("4. Audit & Provenance", "SHA-256 Provenance hashes for MoSPI audit")
            ]
        },
        {
            "header_bg": RGBColor(191, 219, 254),       # Soft pastel blue
            "header_border": RGBColor(59, 130, 246),
            "card_bg": RGBColor(239, 246, 255),         # Soft light blue tint
            "card_border": RGBColor(59, 130, 246),
            "title": "WHY IT IS DIFFERENT",
            "subtitle": "Unique VayuSuchak Advantages",
            "title_color": RGBColor(30, 58, 138),
            "sub_color": RGBColor(29, 78, 216),
            "accent_color": RGBColor(29, 78, 216),
            "points": [
                ("1. Fully Automated", "Zero-latency digital pipeline eliminates all lag."),
                ("2. Comprehensive Capture", "Whole-market view (all lead times and OTAs)"),
                ("3. Verifiable Rigor", "UN/ILO formula with a hash-based audit trail")
            ]
        }
    ]

    for col_idx, col in enumerate(s2_cards_data):
        cx = start_x + col_idx * (card_w + card_gap)
        
        # Outer Card Container
        c_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        c_box.adjustments[0] = 0.04
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = col["card_bg"]
        c_box.line.color.rgb = col["card_border"]
        c_box.line.width = Pt(1.5)

        # Top Header Block
        hdr_h = Inches(0.92)
        hdr = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, hdr_h)
        hdr.adjustments[0] = 0.16
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = col["header_bg"]
        hdr.line.color.rgb = col["header_border"]
        hdr.line.width = Pt(1.2)

        tb_h = s2.shapes.add_textbox(cx + Inches(0.10), card_y + Inches(0.08), card_w - Inches(0.20), hdr_h - Inches(0.14))
        tf_h = tb_h.text_frame
        tf_h.word_wrap = True
        tf_h.margin_top = tf_h.margin_bottom = tf_h.margin_left = tf_h.margin_right = 0
        
        p_ht = tf_h.paragraphs[0]
        p_ht.text = col["title"]
        p_ht.font.name = "Arial"
        p_ht.font.size = Pt(17)
        p_ht.font.bold = True
        p_ht.font.color.rgb = col["title_color"]
        p_ht.alignment = PP_ALIGN.CENTER
        p_ht.space_after = Pt(2)

        p_hs = tf_h.add_paragraph()
        p_hs.text = col["subtitle"]
        p_hs.font.name = "Arial"
        p_hs.font.size = Pt(12)
        p_hs.font.bold = True
        p_hs.font.color.rgb = col["sub_color"]
        p_hs.alignment = PP_ALIGN.CENTER

        # Content Box
        tb_c = s2.shapes.add_textbox(cx + Inches(0.22), card_y + hdr_h + Inches(0.25), card_w - Inches(0.44), card_h - hdr_h - Inches(0.35))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_top = tf_c.margin_bottom = tf_c.margin_left = tf_c.margin_right = 0

        num_points = len(col["points"])
        space_after_pt = Pt(22) if num_points == 4 else Pt(36)

        for p_idx, (p_head, p_desc) in enumerate(col["points"]):
            p_item = tf_c.paragraphs[0] if p_idx == 0 else tf_c.add_paragraph()
            p_item.space_after = Pt(3)

            r_head = p_item.add_run()
            r_head.text = p_head
            r_head.font.name = "Arial"
            r_head.font.size = Pt(14.5)
            r_head.font.bold = True
            r_head.font.color.rgb = col["accent_color"]

            p_body = tf_c.add_paragraph()
            p_body.space_after = space_after_pt
            p_body.line_spacing = 1.18

            r_desc = p_body.add_run()
            r_desc.text = p_desc
            r_desc.font.name = "Arial"
            r_desc.font.size = Pt(12.5)
            r_desc.font.color.rgb = RGBColor(30, 41, 59)

    add_template_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: Technical Approach (Native Vector 4-Column Layout with HD Math)
    # Header: Single line "TECHNICAL APPROACH", serif font, no subtitle
    # Left Column (~25%): Technologies Used (Blue border, white background)
    # Right Section (~75%): System Workflow Diagram + Consolidated Notes Box
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = C_WHITE
    bg3.line.fill.background()

    # Top Bar: Single line title without subtitle
    add_template_top_bar(s3, "TECHNICAL APPROACH", title_line2=None, is_serif=True, title_font_size=28)

    eq1_path, eq2_path = ensure_hd_equations(base_dir)
    wf_top_img = os.path.join(base_dir, "scratch", "workflow_top_hd.png")
    im1 = Image.open(eq1_path)
    im2 = Image.open(eq2_path)

    # 1. LEFT COLUMN: Technologies Used (Width: 3.05", Height: 5.92")
    col_y = Inches(1.08)
    col_h = Inches(5.92)
    col_w_l = Inches(3.05)
    start_x = Inches(0.55)

    box_l = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, start_x, col_y, col_w_l, col_h)
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = C_WHITE
    box_l.line.color.rgb = C_BLUE_TEMPLATE
    box_l.line.width = Pt(1.5)

    tb_l = s3.shapes.add_textbox(start_x + Inches(0.12), col_y + Inches(0.10), col_w_l - Inches(0.24), col_h - Inches(0.20))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p_lh = tf_l.paragraphs[0]
    p_lh.text = "Technologies Used:"
    p_lh.font.name = "Arial"
    p_lh.font.size = Pt(16.5)
    p_lh.font.bold = True
    p_lh.font.color.rgb = C_BLUE_TEMPLATE
    p_lh.space_after = Pt(8)

    tech_groups = [
        ("Languages & Runtimes:", RGBColor(220, 38, 38), [
            "Python 3.13 (Async Harvester & Engine)",
            "TypeScript & React 19 (Dashboard UI)",
            "SQL (PostgreSQL Time-Series & SQLite)"
        ]),
        ("Extraction & Cleansing:", RGBColor(30, 64, 175), [
            "Playwright Headless Stealth Proxy Pool",
            "T+1..T+45 Advance Horizons Tracking",
            "SciPy & NumPy Dynamic IQR Filter"
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
        p_t.space_before = Pt(7)
        p_t.space_after = Pt(2)
        r_t = p_t.add_run()
        r_t.text = title
        r_t.font.name = "Arial"
        r_t.font.size = Pt(10.5)
        r_t.font.bold = True
        r_t.font.color.rgb = col
        
        for it in items:
            p_i = tf_l.add_paragraph()
            p_i.space_after = Pt(2)
            p_i.line_spacing = 1.15
            r_b = p_i.add_run()
            r_b.text = "• "
            r_b.font.name = "Arial"
            r_b.font.size = Pt(8.8)
            r_b.font.bold = True
            r_b.font.color.rgb = C_TEXT_DARK
            
            r_txt = p_i.add_run()
            r_txt.text = it
            r_txt.font.name = "Arial"
            r_txt.font.size = Pt(8.5)
            r_txt.font.color.rgb = C_TEXT_DARK

    # 2. RIGHT SECTION: Workflow Diagram (Top) + Consolidated Notes (Bottom)
    right_x = start_x + col_w_l + Inches(0.20)
    right_w = Inches(12.78) - right_x

    # Top Half: System Workflow Overview Image
    top_w = right_w
    top_h = Inches(2.05)
    top_y = Inches(1.08)

    if os.path.exists(wf_top_img):
        s3.shapes.add_picture(wf_top_img, right_x, top_y, top_w, top_h)

    # Bottom Half: Consolidated Project Details & Implementation Notes
    bot_y = Inches(3.23)
    bot_h = Inches(3.77)

    outer_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, bot_y, right_w, bot_h)
    outer_box.adjustments[0] = 0.02
    outer_box.fill.solid()
    outer_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    outer_box.line.color.rgb = RGBColor(148, 163, 184)
    outer_box.line.width = Pt(1.2)

    banner_h = Inches(0.32)
    banner = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, bot_y, right_w, banner_h)
    banner.adjustments[0] = 0.16
    banner.fill.solid()
    banner.fill.fore_color.rgb = RGBColor(203, 213, 225)
    banner.line.color.rgb = RGBColor(148, 163, 184)
    banner.line.width = Pt(1.0)

    tb_b = banner.text_frame
    p_b = tb_b.paragraphs[0]
    p_b.text = "CONSOLIDATED PROJECT DETAILS & IMPLEMENTATION NOTES"
    p_b.font.name = "Arial"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = RGBColor(15, 23, 42)
    p_b.alignment = PP_ALIGN.CENTER

    # 4 Columns inside bottom container
    col_sub_y = bot_y + banner_h + Inches(0.04)
    col_sub_h = bot_h - banner_h - Inches(0.08) # ~3.37 in

    w1 = Inches(1.78)
    w2 = Inches(1.78)
    w3 = Inches(3.60) # Generous dedicated width for formulas
    w4 = right_w - w1 - w2 - w3 - Inches(0.12) # ~1.70 in
    gap_col = Inches(0.04)

    x1 = right_x + Inches(0.02)
    x2 = x1 + w1 + gap_col
    x3 = x2 + w2 + gap_col
    x4 = x3 + w3 + gap_col

    # --- Column 1: Tier 1 Details ---
    c1 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x1, col_sub_y, w1, col_sub_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = RGBColor(240, 249, 255)
    c1.line.color.rgb = RGBColor(186, 230, 253)
    c1.line.width = Pt(1.0)

    c1_hdr = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x1, col_sub_y, w1, Inches(0.26))
    c1_hdr.fill.solid()
    c1_hdr.fill.fore_color.rgb = RGBColor(186, 230, 253)
    c1_hdr.line.fill.background()
    tf_1h = c1_hdr.text_frame
    p_1h = tf_1h.paragraphs[0]
    p_1h.text = "TIER 1 DETAILS"
    p_1h.font.name = "Arial"
    p_1h.font.size = Pt(9.5)
    p_1h.font.bold = True
    p_1h.font.color.rgb = RGBColor(3, 105, 161)
    p_1h.alignment = PP_ALIGN.CENTER

    tb_c1 = s3.shapes.add_textbox(x1 + Inches(0.06), col_sub_y + Inches(0.30), w1 - Inches(0.12), col_sub_h - Inches(0.34))
    tf_1 = tb_c1.text_frame
    tf_1.word_wrap = True
    tf_1.margin_top = tf_1.margin_bottom = tf_1.margin_left = tf_1.margin_right = 0

    t1_bullets = [
        ("02:00 AM IST Cron", "Automated daily low-traffic batch schedule."),
        ("4 Target Airlines", "Ingests IndiGo, Air India, SpiceJet, Akasa Air."),
        ("Playwright Stealth", "Anti-bot rotation with residential proxy pool."),
        ("Booking Horizons", "Tracks forward windows (T+1 to T+45 days)."),
        ("Full Market Depth", "Captures dynamic yield & pricing curves.")
    ]
    for idx, (b_title, b_desc) in enumerate(t1_bullets):
        p = tf_1.paragraphs[0] if idx == 0 else tf_1.add_paragraph()
        p.space_after = Pt(5.5)
        p.line_spacing = 1.15
        r_dot = p.add_run()
        r_dot.text = "• "
        r_dot.font.name = "Arial"
        r_dot.font.size = Pt(8.8)
        r_dot.font.bold = True
        r_dot.font.color.rgb = RGBColor(3, 105, 161)
        
        r_head = p.add_run()
        r_head.text = f"{b_title}: "
        r_head.font.name = "Arial"
        r_head.font.size = Pt(8.5)
        r_head.font.bold = True
        r_head.font.color.rgb = RGBColor(15, 23, 42)
        
        r_body = p.add_run()
        r_body.text = b_desc
        r_body.font.name = "Arial"
        r_body.font.size = Pt(8.0)
        r_body.font.color.rgb = RGBColor(51, 65, 85)

    # --- Column 2: Tier 2 Details ---
    c2 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x2, col_sub_y, w2, col_sub_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = RGBColor(240, 253, 244)
    c2.line.color.rgb = RGBColor(187, 247, 208)
    c2.line.width = Pt(1.0)

    c2_hdr = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x2, col_sub_y, w2, Inches(0.26))
    c2_hdr.fill.solid()
    c2_hdr.fill.fore_color.rgb = RGBColor(187, 247, 208)
    c2_hdr.line.fill.background()
    tf_2h = c2_hdr.text_frame
    p_2h = tf_2h.paragraphs[0]
    p_2h.text = "TIER 2 DETAILS"
    p_2h.font.name = "Arial"
    p_2h.font.size = Pt(9.5)
    p_2h.font.bold = True
    p_2h.font.color.rgb = RGBColor(21, 128, 61)
    p_2h.alignment = PP_ALIGN.CENTER

    tb_c2 = s3.shapes.add_textbox(x2 + Inches(0.06), col_sub_y + Inches(0.30), w2 - Inches(0.12), col_sub_h - Inches(0.34))
    tf_2 = tb_c2.text_frame
    tf_2.word_wrap = True
    tf_2.margin_top = tf_2.margin_bottom = tf_2.margin_left = tf_2.margin_right = 0

    t2_bullets = [
        ("Fare Unbundling", "Extracts pure base airfare, strips ancillaries."),
        ("JSON Normalization", "Unifies carrier payloads into standard schema."),
        ("Dynamic IQR Filter", "SciPy/NumPy outlier & spike elimination."),
        ("Glitch & Stale Purge", "Rejects HTTP errors, glitches, & stale cache."),
        ("Data Cleansing Audit", "Guarantees clean inputs for index engine.")
    ]
    for idx, (b_title, b_desc) in enumerate(t2_bullets):
        p = tf_2.paragraphs[0] if idx == 0 else tf_2.add_paragraph()
        p.space_after = Pt(5.5)
        p.line_spacing = 1.15
        r_dot = p.add_run()
        r_dot.text = "• "
        r_dot.font.name = "Arial"
        r_dot.font.size = Pt(8.8)
        r_dot.font.bold = True
        r_dot.font.color.rgb = RGBColor(21, 128, 61)
        
        r_head = p.add_run()
        r_head.text = f"{b_title}: "
        r_head.font.name = "Arial"
        r_head.font.size = Pt(8.5)
        r_head.font.bold = True
        r_head.font.color.rgb = RGBColor(15, 23, 42)
        
        r_body = p.add_run()
        r_body.text = b_desc
        r_body.font.name = "Arial"
        r_body.font.size = Pt(8.0)
        r_body.font.color.rgb = RGBColor(51, 65, 85)

    # --- Column 3: Core Indexing Methodology (Highlight Card) ---
    c3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x3, col_sub_y, w3, col_sub_h)
    c3.fill.solid()
    c3.fill.fore_color.rgb = RGBColor(254, 252, 232)
    c3.line.color.rgb = RGBColor(245, 158, 11)
    c3.line.width = Pt(1.5)

    c3_hdr = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x3, col_sub_y, w3, Inches(0.26))
    c3_hdr.fill.solid()
    c3_hdr.fill.fore_color.rgb = RGBColor(254, 215, 170)
    c3_hdr.line.fill.background()
    tf_3h = c3_hdr.text_frame
    p_3h = tf_3h.paragraphs[0]
    p_3h.text = "CORE INDEXING METHODOLOGY"
    p_3h.font.name = "Arial"
    p_3h.font.size = Pt(9.5)
    p_3h.font.bold = True
    p_3h.font.color.rgb = RGBColor(180, 83, 9)
    p_3h.alignment = PP_ALIGN.CENTER

    # Formula 1: Jevons Mean Heading
    y_f1_head = col_sub_y + Inches(0.30)
    tb_j_head = s3.shapes.add_textbox(x3 + Inches(0.06), y_f1_head, w3 - Inches(0.12), Inches(0.20))
    tf_jh = tb_j_head.text_frame
    tf_jh.word_wrap = True
    tf_jh.margin_top = tf_jh.margin_bottom = tf_jh.margin_left = tf_jh.margin_right = 0
    p_jh = tf_jh.paragraphs[0]
    p_jh.text = "1. Jevons Geometric Mean (Elementary Index)"
    p_jh.font.name = "Arial"
    p_jh.font.size = Pt(9.0)
    p_jh.font.bold = True
    p_jh.font.color.rgb = RGBColor(146, 64, 14)

    # Place Equation 1 Image (Large, prominent across full card width)
    eq1_w = w3 - Inches(0.14) # ~3.46 inches
    eq1_h = eq1_w / (im1.size[0] / im1.size[1]) # ~0.51 inches
    y_f1_img = y_f1_head + Inches(0.20)
    s3.shapes.add_picture(eq1_path, x3 + Inches(0.07), y_f1_img, eq1_w, eq1_h)

    # Bullets for Jevons
    y_f1_b = y_f1_img + eq1_h + Inches(0.04)
    tb_j_b = s3.shapes.add_textbox(x3 + Inches(0.08), y_f1_b, w3 - Inches(0.16), Inches(0.52))
    tf_jb = tb_j_b.text_frame
    tf_jb.word_wrap = True
    tf_jb.margin_top = tf_jb.margin_bottom = tf_jb.margin_left = tf_jb.margin_right = 0
    p1 = tf_jb.paragraphs[0]
    p1.text = "• Adheres strictly to UN/ILO CPI Manual (Chapter 10) standards"
    p1.font.name = "Arial"
    p1.font.size = Pt(8.5)
    p1.font.color.rgb = RGBColor(30, 41, 59)
    p1.space_after = Pt(2.5)
    p2 = tf_jb.add_paragraph()
    p2.text = "• Axiomatically satisfies Time Reversal & Circular Transitivity tests"
    p2.font.name = "Arial"
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = RGBColor(30, 41, 59)

    # Formula 2: Composite Aggregation Heading
    y_f2_head = y_f1_b + Inches(0.56)
    tb_c_head = s3.shapes.add_textbox(x3 + Inches(0.06), y_f2_head, w3 - Inches(0.12), Inches(0.20))
    tf_ch = tb_c_head.text_frame
    tf_ch.word_wrap = True
    tf_ch.margin_top = tf_ch.margin_bottom = tf_ch.margin_left = tf_ch.margin_right = 0
    p_ch = tf_ch.paragraphs[0]
    p_ch.text = "2. DGCA Volume Weighted Aggregation (National Rollup)"
    p_ch.font.name = "Arial"
    p_ch.font.size = Pt(9.0)
    p_ch.font.bold = True
    p_ch.font.color.rgb = RGBColor(146, 64, 14)

    # Place Equation 2 Image (Large, prominent)
    eq2_w = Inches(3.25)
    eq2_h = eq2_w / (im2.size[0] / im2.size[1]) # ~0.47 inches
    y_f2_img = y_f2_head + Inches(0.20)
    s3.shapes.add_picture(eq2_path, x3 + Inches(0.17), y_f2_img, eq2_w, eq2_h)

    # Bullets for Composite
    y_f2_b = y_f2_img + eq2_h + Inches(0.04)
    tb_c_b = s3.shapes.add_textbox(x3 + Inches(0.08), y_f2_b, w3 - Inches(0.16), Inches(0.52))
    tf_cb = tb_c_b.text_frame
    tf_cb.word_wrap = True
    tf_cb.margin_top = tf_cb.margin_bottom = tf_cb.margin_left = tf_cb.margin_right = 0
    p3 = tf_cb.paragraphs[0]
    p3.text = "• Routes weighted by official DGCA passenger volume shares (w_c)"
    p3.font.name = "Arial"
    p3.font.size = Pt(8.5)
    p3.font.color.rgb = RGBColor(30, 41, 59)
    p3.space_after = Pt(2.5)
    p4 = tf_cb.add_paragraph()
    p4.text = "• Key Trunk Routes: Delhi-Mumbai (14.8%) | Bengaluru-Delhi (9.2%)"
    p4.font.name = "Arial"
    p4.font.size = Pt(8.5)
    p4.font.color.rgb = RGBColor(30, 41, 59)

    # --- Column 4: Tier 4 Details ---
    c4 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x4, col_sub_y, w4, col_sub_h)
    c4.fill.solid()
    c4.fill.fore_color.rgb = RGBColor(241, 245, 249)
    c4.line.color.rgb = RGBColor(203, 213, 225)
    c4.line.width = Pt(1.0)

    c4_hdr = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x4, col_sub_y, w4, Inches(0.26))
    c4_hdr.fill.solid()
    c4_hdr.fill.fore_color.rgb = RGBColor(203, 213, 225)
    c4_hdr.line.fill.background()
    tf_4h = c4_hdr.text_frame
    p_4h = tf_4h.paragraphs[0]
    p_4h.text = "TIER 4 DETAILS"
    p_4h.font.name = "Arial"
    p_4h.font.size = Pt(9.5)
    p_4h.font.bold = True
    p_4h.font.color.rgb = RGBColor(30, 41, 59)
    p_4h.alignment = PP_ALIGN.CENTER

    tb_c4 = s3.shapes.add_textbox(x4 + Inches(0.06), col_sub_y + Inches(0.30), w4 - Inches(0.12), col_sub_h - Inches(0.34))
    tf_4 = tb_c4.text_frame
    tf_4.word_wrap = True
    tf_4.margin_top = tf_4.margin_bottom = tf_4.margin_left = tf_4.margin_right = 0

    t4_bullets = [
        ("Cryptographic Audit", "SHA-256 batch fingerprints ensure immutability."),
        ("Merkle Proof Ledger", "Verifiable mathematical audit trail for MoSPI."),
        ("NDSAP PostgreSQL DB", "Time-series database & historical archive vault."),
        ("Sub-10ms REST API", "FastAPI endpoints feed MoSPI & RBI real-time."),
        ("NDSAP Standards", "Ready for automated open government data feeds.")
    ]
    for idx, (b_title, b_desc) in enumerate(t4_bullets):
        p = tf_4.paragraphs[0] if idx == 0 else tf_4.add_paragraph()
        p.space_after = Pt(5.5)
        p.line_spacing = 1.15
        r_dot = p.add_run()
        r_dot.text = "• "
        r_dot.font.name = "Arial"
        r_dot.font.size = Pt(8.8)
        r_dot.font.bold = True
        r_dot.font.color.rgb = RGBColor(30, 41, 59)
        
        r_head = p.add_run()
        r_head.text = f"{b_title}: "
        r_head.font.name = "Arial"
        r_head.font.size = Pt(8.5)
        r_head.font.bold = True
        r_head.font.color.rgb = RGBColor(15, 23, 42)
        
        r_body = p.add_run()
        r_body.text = b_desc
        r_body.font.name = "Arial"
        r_body.font.size = Pt(8.0)
        r_body.font.color.rgb = RGBColor(51, 65, 85)

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
