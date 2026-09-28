import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_reviewed_presentation(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Clean Sovereign Color Palette
    C_WHITE = RGBColor(255, 255, 255)
    C_NAVY_TITLE = RGBColor(27, 54, 93)      # Official SIH dark navy serif
    C_BLUE_SUB = RGBColor(24, 76, 148)       # Elegant blue for subtitles/accents
    C_TEXT_MAIN = RGBColor(30, 41, 59)       # Slate 800
    C_TEXT_MUTED = RGBColor(71, 85, 105)     # Slate 600
    C_BORDER_LIGHT = RGBColor(203, 213, 225) # Slate 300
    C_CARD_BG = RGBColor(248, 250, 252)      # Soft Slate 50
    C_BLUE_BORDER = RGBColor(37, 99, 235)    # Blue border
    C_PURPLE_TECH = RGBColor(109, 40, 217)   # Tech keyword highlight
    C_RED_ACCENT = RGBColor(185, 28, 28)
    C_GREEN_ACCENT = RGBColor(22, 101, 52)
    C_INDIGO_ACCENT = RGBColor(67, 56, 202)

    # Asset paths
    base_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
    pres_dir = os.path.join(base_dir, "public", "presentation")

    logo_sih = os.path.join(pres_dir, "sih_2026_logo_hd.png")
    big_sih_graphic = os.path.join(pres_dir, "sih_cover_badge_hd.png")
    arch_img = os.path.join(pres_dir, "architecture_diagram.png")
    pyramid_img = os.path.join(pres_dir, "pyramid_diagram_page2.png")
    methodology_wheel = os.path.join(pres_dir, "methodology_wheel_page3.png")
    impact_wheel = os.path.join(pres_dir, "impact_wheel_page5.png")
    comparison_chart = os.path.join(pres_dir, "comparison_chart_page5.png")
    runway_banner = os.path.join(pres_dir, "runway_skyline_banner.png")
    surge_callout = os.path.join(pres_dir, "flight_surge_callout.png")
    manual_digital = os.path.join(pres_dir, "manual_to_digital_callout.png")

    def add_top_bar(slide, title_text, subtitle_text=None, show_team=True, title_font_size=23):
        # 1. Team Name Pill on top-left
        if show_team:
            pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.18), Inches(1.8), Inches(0.62))
            pill.adjustments[0] = 0.5
            pill.fill.solid()
            pill.fill.fore_color.rgb = C_WHITE
            pill.line.color.rgb = C_INDIGO_ACCENT
            pill.line.width = Pt(1.5)
            tf_p = pill.text_frame
            tf_p.word_wrap = True
            p_p = tf_p.paragraphs[0]
            p_p.text = "Team Rookie"
            p_p.font.name = "Arial"
            p_p.font.size = Pt(12)
            p_p.font.bold = True
            p_p.font.color.rgb = C_INDIGO_ACCENT
            p_p.alignment = PP_ALIGN.CENTER
            
        # 2. Main Title in the middle (Centered Bold Serif)
        tb_t = slide.shapes.add_textbox(Inches(2.5), Inches(0.10), Inches(8.3), Inches(0.98))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = "Times New Roman"
        p_t.font.size = Pt(title_font_size)
        p_t.font.bold = True
        p_t.font.color.rgb = C_NAVY_TITLE
        p_t.alignment = PP_ALIGN.CENTER
        
        if subtitle_text:
            p_sub = tf_t.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(11)
            p_sub.font.bold = True
            p_sub.font.color.rgb = C_BLUE_SUB
            p_sub.alignment = PP_ALIGN.CENTER

        # 3. Official SIH Logo on top-right
        if os.path.exists(logo_sih):
            slide.shapes.add_picture(logo_sih, Inches(11.1), Inches(0.14), Inches(1.8), Inches(0.85))

    # =========================================================================
    # SLIDE 1: Title Slide (Centered Title, Clean Metadata, SIH Visual Emblem)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_WHITE
    bg1.line.fill.background()

    # Top Center Title
    tb_s1_title = s1.shapes.add_textbox(Inches(0.9), Inches(0.55), Inches(11.5), Inches(1.0))
    tf_s1_title = tb_s1_title.text_frame
    tf_s1_title.word_wrap = True
    p1 = tf_s1_title.paragraphs[0]
    p1.text = "SMART INDIA HACKATHON 2026"
    p1.font.name = "Times New Roman"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = C_NAVY_TITLE
    p1.alignment = PP_ALIGN.CENTER

    tb_badge = s1.shapes.add_textbox(Inches(2.5), Inches(1.4), Inches(8.3), Inches(0.45))
    tf_b = tb_badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "Sovereign Digital Public Infrastructure for MoSPI NSO & RBI Inflation Targeting"
    p_b.font.name = "Arial"
    p_b.font.size = Pt(13)
    p_b.font.bold = True
    p_b.font.color.rgb = C_BLUE_SUB
    p_b.alignment = PP_ALIGN.CENTER

    if os.path.exists(logo_sih):
        s1.shapes.add_picture(logo_sih, Inches(11.1), Inches(0.2), Inches(1.8), Inches(0.9))

    if os.path.exists(big_sih_graphic):
        s1.shapes.add_picture(big_sih_graphic, Inches(8.3), Inches(2.0), Inches(4.3), Inches(4.8))

    s1_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(2.05), Inches(7.2), Inches(4.7))
    s1_card.adjustments[0] = 0.04
    s1_card.fill.solid()
    s1_card.fill.fore_color.rgb = C_CARD_BG
    s1_card.line.color.rgb = C_BORDER_LIGHT
    s1_card.line.width = Pt(1.5)

    tb_s1_meta = s1.shapes.add_textbox(Inches(1.2), Inches(2.25), Inches(6.6), Inches(4.3))
    tf_s1_meta = tb_s1_meta.text_frame
    tf_s1_meta.word_wrap = True
    tf_s1_meta.margin_left = tf_s1_meta.margin_top = tf_s1_meta.margin_right = tf_s1_meta.margin_bottom = 0

    bullets_s1 = [
        ("Problem Statement ID – ", "SIH26056"),
        ("Problem Statement Title – ", "Real-time Airfare Price Index for CPI Augmentation"),
        ("Theme – ", "Smart Governance / Miscellaneous"),
        ("PS Category – ", "Software"),
        ("Team ID – ", "Team Rookie"),
        ("Team Name – ", "Team Rookie")
    ]

    for i, (label, val) in enumerate(bullets_s1):
        p = tf_s1_meta.add_paragraph() if i > 0 else tf_s1_meta.paragraphs[0]
        p.space_after = Pt(14)
        run_bullet = p.add_run()
        run_bullet.text = "• " + label
        run_bullet.font.name = "Arial"
        run_bullet.font.size = Pt(16)
        run_bullet.font.bold = True
        run_bullet.font.color.rgb = RGBColor(15, 23, 42)
        
        run_val = p.add_run()
        run_val.text = val
        run_val.font.name = "Arial"
        run_val.font.size = Pt(16)
        run_val.font.bold = True
        run_val.font.color.rgb = C_BLUE_SUB

    # =========================================================================
    # SLIDE 2: Problem, Solution & Unique Value Proposition (PAGE 2 KUNAL.TECHY STYLE)
    # Left: 3 Context Cards (Real-world Issue, Why Important, Solution) + Prototype Box
    # Center: 4-Tier Pyramid Diagram (pyramid_diagram_page2.png)
    # Right: 3 Risk vs Solution Pills + Surge Callout Graphic
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = C_WHITE
    bg2.line.fill.background()

    add_top_bar(s2, "VAYUSUCHAK: AI-POWERED REAL-TIME AIRFARE PRICE INDEX", "Revolutionizing Transport Inflation Measurement for MoSPI NSO & RBI", show_team=True, title_font_size=21)

    # 1. Left Section: 3 Context Cards
    left_x = Inches(0.55)
    card_w = Inches(3.4)
    
    # Card 1: Real-world Issue
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(1.18), card_w, Inches(1.4))
    c1.adjustments[0] = 0.08
    c1.fill.solid()
    c1.fill.fore_color.rgb = RGBColor(254, 242, 242)
    c1.line.color.rgb = RGBColor(239, 68, 68)
    c1.line.width = Pt(1.5)
    tb1 = s2.shapes.add_textbox(left_x + Inches(0.12), Inches(1.22), card_w - Inches(0.24), Inches(1.3))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0
    p1_h = tf1.paragraphs[0]
    p1_h.text = "🚨 Real-world Issue:"
    p1_h.font.name = "Arial"
    p1_h.font.size = Pt(11)
    p1_h.font.bold = True
    p1_h.font.color.rgb = RGBColor(185, 28, 28)
    p1_t = tf1.add_paragraph()
    p1_t.text = "Manual price-collection visits capture only 1 static quote/month, completely missing 200–400% intraday algorithmic airline price surges across 90%+ online bookings."
    p1_t.font.name = "Arial"
    p1_t.font.size = Pt(9.5)
    p1_t.font.color.rgb = C_TEXT_MAIN

    # Card 2: Why Important
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(2.68), card_w, Inches(1.4))
    c2.adjustments[0] = 0.08
    c2.fill.solid()
    c2.fill.fore_color.rgb = RGBColor(254, 252, 232)
    c2.line.color.rgb = RGBColor(234, 179, 8)
    c2.line.width = Pt(1.5)
    tb2 = s2.shapes.add_textbox(left_x + Inches(0.12), Inches(2.72), card_w - Inches(0.24), Inches(1.3))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = 0
    p2_h = tf2.paragraphs[0]
    p2_h.text = "📊 Why Important:"
    p2_h.font.name = "Arial"
    p2_h.font.size = Pt(11)
    p2_h.font.bold = True
    p2_h.font.color.rgb = RGBColor(180, 83, 9)
    p2_t = tf2.add_paragraph()
    p2_t.text = "Transportation CPI heavily drives RBI Monetary Policy rate-setting. A 15-day manual survey lag creates blindspots in ₹200+ Lakh Cr economic policy decisions."
    p2_t.font.name = "Arial"
    p2_t.font.size = Pt(9.5)
    p2_t.font.color.rgb = C_TEXT_MAIN

    # Card 3: Solution
    c3 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(4.18), card_w, Inches(1.4))
    c3.adjustments[0] = 0.08
    c3.fill.solid()
    c3.fill.fore_color.rgb = RGBColor(240, 253, 244)
    c3.line.color.rgb = RGBColor(34, 197, 94)
    c3.line.width = Pt(1.5)
    tb3 = s2.shapes.add_textbox(left_x + Inches(0.12), Inches(4.22), card_w - Inches(0.24), Inches(1.3))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_right = tf3.margin_top = tf3.margin_bottom = 0
    p3_h = tf3.paragraphs[0]
    p3_h.text = "💡 Solution:"
    p3_h.font.name = "Arial"
    p3_h.font.size = Pt(11)
    p3_h.font.bold = True
    p3_h.font.color.rgb = RGBColor(21, 128, 61)
    p3_t = tf3.add_paragraph()
    p3_t.text = "Autonomous Playwright harvesting of 10,000+ daily fares + UN/ILO Jevons geometric mean index + SHA-256 cryptographic audit provenance delivered via Vercel Edge."
    p3_t.font.name = "Arial"
    p3_t.font.size = Pt(9.5)
    p3_t.font.color.rgb = C_TEXT_MAIN

    # Left Bottom Prototype Box
    c_proto = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(5.72), card_w, Inches(1.5))
    c_proto.adjustments[0] = 0.12
    c_proto.fill.solid()
    c_proto.fill.fore_color.rgb = RGBColor(239, 246, 255)
    c_proto.line.color.rgb = RGBColor(59, 130, 246)
    c_proto.line.width = Pt(1.5)
    tb_pr = s2.shapes.add_textbox(left_x + Inches(0.15), Inches(5.78), card_w - Inches(0.3), Inches(1.4))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True
    p_pr1 = tf_pr.paragraphs[0]
    p_pr1.text = "☁️ Working Prototype:"
    p_pr1.font.name = "Arial"
    p_pr1.font.size = Pt(11)
    p_pr1.font.bold = True
    p_pr1.font.color.rgb = RGBColor(29, 78, 216)
    p_pr2 = tf_pr.add_paragraph()
    p_pr2.text = "• Live Portal: airintel.vercel.app\n• Swagger REST API: /api/v1/apix/*\n• 100% Automated Daily Scheduled Cron"
    p_pr2.font.name = "Arial"
    p_pr2.font.size = Pt(9.5)
    p_pr2.font.color.rgb = C_TEXT_MAIN

    # 2. Center: 4-Tier Pyramid Diagram
    if os.path.exists(pyramid_img):
        s2.shapes.add_picture(pyramid_img, Inches(4.08), Inches(1.15), Inches(5.24), Inches(6.1))

    # 3. Right Side: 3 Risk vs Solution Pills + Surge Callout Graphic
    right_x = Inches(9.45)
    right_w = Inches(3.4)

    # Header: Risk VS Solution
    tb_rvs = s2.shapes.add_textbox(right_x, Inches(1.12), right_w, Inches(0.32))
    tf_rvs = tb_rvs.text_frame
    p_rvs = tf_rvs.paragraphs[0]
    p_rvs.text = "Risk                     VS                     Solution"
    p_rvs.font.name = "Arial"
    p_rvs.font.size = Pt(11)
    p_rvs.font.bold = True
    p_rvs.font.color.rgb = C_NAVY_TITLE
    p_rvs.alignment = PP_ALIGN.CENTER

    risk_solutions = [
        ("Endless Intraday Surges", "Real-Time Yield Capture"),
        ("Upward Substitution Bias", "UN/ILO Jevons Formula"),
        ("Anti-Scraping / DOM Drifts", "Stealth Crawlers & Schemas")
    ]

    for idx, (risk_txt, sol_txt) in enumerate(risk_solutions):
        ry = Inches(1.48) + idx * Inches(0.92)
        
        # Risk Pill (Red)
        r_pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, ry, Inches(1.5), Inches(0.72))
        r_pill.adjustments[0] = 0.35
        r_pill.fill.solid()
        r_pill.fill.fore_color.rgb = RGBColor(239, 68, 68)
        r_pill.line.fill.background()
        tf_rp = r_pill.text_frame
        tf_rp.word_wrap = True
        tf_rp.margin_left = tf_rp.margin_right = tf_rp.margin_top = tf_rp.margin_bottom = Inches(0.04)
        p_rp = tf_rp.paragraphs[0]
        p_rp.text = "⛔ " + risk_txt
        p_rp.font.name = "Arial"
        p_rp.font.size = Pt(8.5)
        p_rp.font.bold = True
        p_rp.font.color.rgb = C_WHITE
        p_rp.alignment = PP_ALIGN.CENTER

        # Connector symbol
        tb_conn = s2.shapes.add_textbox(right_x + Inches(1.52), ry + Inches(0.16), Inches(0.36), Inches(0.4))
        tf_conn = tb_conn.text_frame
        p_conn = tf_conn.paragraphs[0]
        p_conn.text = "⟷"
        p_conn.font.name = "Arial"
        p_conn.font.size = Pt(12)
        p_conn.font.bold = True
        p_conn.font.color.rgb = RGBColor(100, 116, 139)
        p_conn.alignment = PP_ALIGN.CENTER

        # Solution Pill (Green)
        s_pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x + Inches(1.9), ry, Inches(1.5), Inches(0.72))
        s_pill.adjustments[0] = 0.35
        s_pill.fill.solid()
        s_pill.fill.fore_color.rgb = RGBColor(34, 197, 94)
        s_pill.line.fill.background()
        tf_sp = s_pill.text_frame
        tf_sp.word_wrap = True
        tf_sp.margin_left = tf_sp.margin_right = tf_sp.margin_top = tf_sp.margin_bottom = Inches(0.04)
        p_sp = tf_sp.paragraphs[0]
        p_sp.text = "✅ " + sol_txt
        p_sp.font.name = "Arial"
        p_sp.font.size = Pt(8.5)
        p_sp.font.bold = True
        p_sp.font.color.rgb = C_WHITE
        p_sp.alignment = PP_ALIGN.CENTER

    # Right Bottom: Flight Surge Graphic Callout
    if os.path.exists(surge_callout):
        s2.shapes.add_picture(surge_callout, right_x + Inches(0.2), Inches(4.35), Inches(3.0), Inches(2.85))

    # =========================================================================
    # SLIDE 3: Technical Approach (PAGE 3 KUNAL.TECHY STYLE)
    # Left: Methodology & Process Implementation Lifecycle Wheel + GitHub Box
    # Center: Process Flow Architecture Diagram
    # Right: Top System Audit & Provenance + Bottom Technologies Used
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg3.fill.solid()
    bg3.fill.fore_color.rgb = C_WHITE
    bg3.line.fill.background()

    add_top_bar(s3, "TECHNICAL APPROACH", "BUILDING SOVEREIGN DIGITAL PUBLIC INFRASTRUCTURE WITH PRECISION", show_team=True)

    # 1. Left Box: Methodology & Implementation Wheel
    left_c3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(1.15), Inches(4.2), Inches(6.1))
    left_c3.adjustments[0] = 0.04
    left_c3.fill.solid()
    left_c3.fill.fore_color.rgb = C_WHITE
    left_c3.line.color.rgb = C_BLUE_BORDER
    left_c3.line.width = Pt(1.5)

    # Header
    tb_m_head = s3.shapes.add_textbox(Inches(0.60), Inches(1.22), Inches(4.1), Inches(0.4))
    tf_mh = tb_m_head.text_frame
    p_mh = tf_mh.paragraphs[0]
    p_mh.text = "METHODOLOGY & PROCESS OF IMPLEMENTATION"
    p_mh.font.name = "Arial"
    p_mh.font.size = Pt(9.5)
    p_mh.font.bold = True
    p_mh.font.color.rgb = RGBColor(30, 58, 138)
    p_mh.alignment = PP_ALIGN.CENTER

    # Wheel image inside
    if os.path.exists(methodology_wheel):
        s3.shapes.add_picture(methodology_wheel, Inches(0.68), Inches(1.68), Inches(3.95), Inches(4.2))

    # Bottom Report Callout inside Left Box
    rep_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(6.0), Inches(3.6), Inches(1.05))
    rep_box.adjustments[0] = 0.15
    rep_box.fill.solid()
    rep_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    rep_box.line.color.rgb = C_BORDER_LIGHT
    rep_box.line.width = Pt(1.0)
    tb_rep = s3.shapes.add_textbox(Inches(0.95), Inches(6.05), Inches(3.4), Inches(0.95))
    tf_rep = tb_rep.text_frame
    tf_rep.word_wrap = True
    p_rep1 = tf_rep.paragraphs[0]
    p_rep1.text = "📋 Detailed Technical Report & Open Code"
    p_rep1.font.name = "Arial"
    p_rep1.font.size = Pt(9.5)
    p_rep1.font.bold = True
    p_rep1.font.color.rgb = C_NAVY_TITLE
    p_rep1.alignment = PP_ALIGN.CENTER
    p_rep2 = tf_rep.add_paragraph()
    p_rep2.text = "github.com/TeamRookie/AirIntel-India\nConforming to NDSAP Sovereign Open Data Standard"
    p_rep2.font.name = "Arial"
    p_rep2.font.size = Pt(8.5)
    p_rep2.font.color.rgb = RGBColor(71, 85, 105)
    p_rep2.alignment = PP_ALIGN.CENTER

    # 2. Center: Process Flow Architecture
    center_c3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.9), Inches(1.15), Inches(4.3), Inches(6.1))
    center_c3.adjustments[0] = 0.04
    center_c3.fill.solid()
    center_c3.fill.fore_color.rgb = C_WHITE
    center_c3.line.color.rgb = C_BLUE_BORDER
    center_c3.line.width = Pt(1.5)

    tb_flow_t = s3.shapes.add_textbox(Inches(5.0), Inches(1.22), Inches(4.1), Inches(0.4))
    tf_ft = tb_flow_t.text_frame
    p_ft = tf_ft.paragraphs[0]
    p_ft.text = "END-TO-END SYSTEM PIPELINE"
    p_ft.font.name = "Arial"
    p_ft.font.size = Pt(10.5)
    p_ft.font.bold = True
    p_ft.font.color.rgb = RGBColor(30, 58, 138)
    p_ft.alignment = PP_ALIGN.CENTER

    if os.path.exists(arch_img):
        s3.shapes.add_picture(arch_img, Inches(4.98), Inches(1.68), Inches(4.14), Inches(5.45))

    # 3. Right Section: Top Audit Box & Bottom Technologies Used
    right_c3_x = Inches(9.35)
    right_c3_w = Inches(3.45)

    # Top Audit Box
    audit_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_c3_x, Inches(1.15), right_c3_w, Inches(2.2))
    audit_card.adjustments[0] = 0.06
    audit_card.fill.solid()
    audit_card.fill.fore_color.rgb = RGBColor(248, 250, 252)
    audit_card.line.color.rgb = RGBColor(99, 102, 241)
    audit_card.line.width = Pt(1.5)

    tb_aud = s3.shapes.add_textbox(right_c3_x + Inches(0.12), Inches(1.22), right_c3_w - Inches(0.24), Inches(2.0))
    tf_aud = tb_aud.text_frame
    tf_aud.word_wrap = True
    p_ah = tf_aud.paragraphs[0]
    p_ah.text = "🔒 AUDIT & PROVENANCE VAULT"
    p_ah.font.name = "Arial"
    p_ah.font.size = Pt(10)
    p_ah.font.bold = True
    p_ah.font.color.rgb = RGBColor(67, 56, 202)
    p_ah.alignment = PP_ALIGN.CENTER

    p_at = tf_aud.add_paragraph()
    p_at.text = "• SHA-256 Batch Hashes: Immutable root fingerprint generated per harvest batch.\n• Anti-Tamper Verification: Evidentiary legal audit standard for MoSPI & courts.\n• NDSAP Conformance: Full metadata schemas preserved for retrospective audits."
    p_at.font.name = "Arial"
    p_at.font.size = Pt(8.5)
    p_at.font.color.rgb = C_TEXT_MAIN

    # Bottom Technologies Used Box
    tech_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_c3_x, Inches(3.48), right_c3_w, Inches(3.77))
    tech_box.adjustments[0] = 0.05
    tech_box.fill.solid()
    tech_box.fill.fore_color.rgb = C_WHITE
    tech_box.line.color.rgb = C_BORDER_LIGHT
    tech_box.line.width = Pt(1.5)

    tb_tech_t = s3.shapes.add_textbox(right_c3_x + Inches(0.1), Inches(3.55), right_c3_w - Inches(0.2), Inches(0.3))
    tf_tt = tb_tech_t.text_frame
    p_tt = tf_tt.paragraphs[0]
    p_tt.text = "TECHNOLOGIES USED"
    p_tt.font.name = "Arial"
    p_tt.font.size = Pt(10.5)
    p_tt.font.bold = True
    p_tt.font.color.rgb = C_NAVY_TITLE
    p_tt.alignment = PP_ALIGN.CENTER

    tech_pills = [
        ("FrontEnd", "React 19, TailwindCSS, Lucide Icons, Recharts Analytics", RGBColor(14, 165, 233), RGBColor(240, 249, 255)),
        ("BackEnd", "Python 3.13, FastAPI, Playwright Headless, NumPy", RGBColor(16, 185, 129), RGBColor(240, 253, 244)),
        ("Deployment", "Vercel Edge Serverless, GitHub Actions Cron", RGBColor(168, 85, 247), RGBColor(250, 245, 255)),
        ("Engines", "UN/ILO Jevons Formula, SciPy IQR, SHA-256 Vault", RGBColor(245, 158, 11), RGBColor(254, 252, 232))
    ]

    for tidx, (cat, stack, col_border, col_bg) in enumerate(tech_pills):
        tp_y = Inches(3.92) + tidx * Inches(0.78)
        tp_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_c3_x + Inches(0.15), tp_y, right_c3_w - Inches(0.3), Inches(0.7))
        tp_card.adjustments[0] = 0.2
        tp_card.fill.solid()
        tp_card.fill.fore_color.rgb = col_bg
        tp_card.line.color.rgb = col_border
        tp_card.line.width = Pt(1.2)

        tb_tp = s3.shapes.add_textbox(right_c3_x + Inches(0.22), tp_y + Inches(0.06), right_c3_w - Inches(0.44), Inches(0.58))
        tf_tp = tb_tp.text_frame
        tf_tp.word_wrap = True
        tf_tp.margin_left = tf_tp.margin_right = tf_tp.margin_top = tf_tp.margin_bottom = 0
        p_cat = tf_tp.paragraphs[0]
        p_cat.text = "⚡ " + cat
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = col_border
        p_st = tf_tp.add_paragraph()
        p_st.text = stack
        p_st.font.name = "Arial"
        p_st.font.size = Pt(8.5)
        p_st.font.color.rgb = RGBColor(51, 65, 85)

    # =========================================================================
    # SLIDE 4: Feasibility and Viability (PAGE 4 KUNAL.TECHY STYLE)
    # 3 Vertical Columns (Feasibility Analysis, Viability, Business Potential)
    # 4 distinct icon cards per column + Bottom Runway Skyline Banner
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg4.fill.solid()
    bg4.fill.fore_color.rgb = C_WHITE
    bg4.line.fill.background()

    add_top_bar(s4, "FEASIBILITY AND VIABILITY", "PRACTICAL • SCALABLE • SUSTAINABLE IMPACT", show_team=True)

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
        c_col = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.15), col_w, Inches(4.9))
        c_col.adjustments[0] = 0.03
        c_col.fill.solid()
        c_col.fill.fore_color.rgb = RGBColor(255, 255, 255)
        c_col.line.color.rgb = theme_col
        c_col.line.width = Pt(1.5)

        # Column Header Banner
        h_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.15), col_w, Inches(0.58))
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
            card_y = Inches(1.82) + c_idx * Inches(1.02)
            card_shape = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.12), card_y, col_w - Inches(0.24), Inches(0.94))
            card_shape.adjustments[0] = 0.12
            card_shape.fill.solid()
            card_shape.fill.fore_color.rgb = bg_col
            card_shape.line.color.rgb = theme_col
            card_shape.line.width = Pt(1.0)

            tb_cd = s4.shapes.add_textbox(cx + Inches(0.18), card_y + Inches(0.06), col_w - Inches(0.36), Inches(0.82))
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
            p_cb.font.color.rgb = C_TEXT_MAIN

    # Bottom Runway Skyline Banner spanning the bottom width
    if os.path.exists(runway_banner):
        s4.shapes.add_picture(runway_banner, Inches(0.65), Inches(6.15), Inches(12.02), Inches(1.22))

    # =========================================================================
    # SLIDE 5: Impact and Benefits (PAGE 5 KUNAL.TECHY STYLE)
    # Left: Circular Impacts & Benefits Wheel (impact_wheel_page5.png)
    # Right Top: Comparative Horizontal Bar Chart (comparison_chart_page5.png)
    # Right Bottom: From Manual Quotes -> Real-Time Intelligence Callout
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg5.fill.solid()
    bg5.fill.fore_color.rgb = C_WHITE
    bg5.line.fill.background()

    add_top_bar(s5, "IMPACT AND BENEFITS", "TRANSFORMING SOVEREIGN ECONOMIC GOVERNANCE & POLICY RESPONSIVENESS", show_team=True)

    # 1. Left Side: Circular Impacts & Benefits Wheel
    if os.path.exists(impact_wheel):
        s5.shapes.add_picture(impact_wheel, Inches(0.65), Inches(1.18), Inches(6.3), Inches(6.05))

    # 2. Right Side Top: Comparative Horizontal Bar Chart
    if os.path.exists(comparison_chart):
        s5.shapes.add_picture(comparison_chart, Inches(7.15), Inches(1.18), Inches(5.6), Inches(3.7))

    # 3. Right Side Bottom: Manual to Digital Callout
    if os.path.exists(manual_digital):
        s5.shapes.add_picture(manual_digital, Inches(7.15), Inches(5.0), Inches(5.6), Inches(2.2))

    # =========================================================================
    # SLIDE 6: Research and References (4-QUADRANT VISUAL CITATION MATRIX)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = C_WHITE
    bg6.line.fill.background()

    add_top_bar(s6, "RESEARCH AND REFERENCES", "Academic Foundations, Official Data Sources & Technical Documentation", show_team=True)

    quads = [
        (
            Inches(0.8), Inches(1.3), Inches(5.6), Inches(2.75),
            "SUPPORTING RESEARCH PAPERS",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                "Cavallo, A., & Rigobon, R. (2016). 'The Billion Prices Project: Using Online Data for Measurement and Research.' Journal of Economic Perspectives, 30(2), 151-178.",
                "UN, ILO, IMF, OECD, Eurostat, World Bank (2020). Consumer Price Index Manual: Concepts and Methods, Chapter 10 (Elementary Indices).",
                "Diewert, W. E. (2004). 'Elementary Indices.' In Consumer Price Index Theory, IMF Handbook."
            ]
        ),
        (
            Inches(6.9), Inches(1.3), Inches(5.6), Inches(2.75),
            "OFFICIAL DATA SOURCES",
            RGBColor(15, 23, 42), RGBColor(241, 245, 249),
            [
                "DGCA India: Monthly Scheduled Domestic Passenger Traffic (dgca.gov.in)",
                "MoSPI NSO: Consumer Price Index Concepts & Guidelines (mospi.gov.in)",
                "Direct Airline Booking Portals: Air India, IndiGo, Akasa, SpiceJet",
                "Online Travel Aggregators: MakeMyTrip, EaseMyTrip Non-Stop Pricing Feeds"
            ]
        ),
        (
            Inches(0.8), Inches(4.25), Inches(5.6), Inches(2.85),
            "MARKET RESEARCH & MOTIVATION",
            RGBColor(15, 23, 42), RGBColor(241, 245, 249),
            [
                "Indian domestic air passenger traffic projected to grow at >15% CAGR (2024–2030).",
                "Algorithmic dynamic pricing generates 200–400% intraday fare volatility across key metro routes.",
                "Over 90% of domestic air tickets sold digitally, making physical airport surveying obsolete.",
                "VayuSuchak eliminates the critical 15-day MoSPI manual survey reporting lag with zero latency."
            ]
        ),
        (
            Inches(6.9), Inches(4.25), Inches(5.6), Inches(2.85),
            "TECHNICAL DOCUMENTATION & SPECS",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                "Index Formulations: UN/ILO Jevons Geometric Mean mathematically proven to eliminate Dutot upward bias.",
                "Harvester Engine: Playwright Chromium Headless with ethical crawl delays and Cloudflare stealth evasion.",
                "Provenance Vault: SHA-256 Hash Manifest conforming to National Data Sharing & Accessibility Policy (NDSAP).",
                "Deployment Architecture: Serverless cron pipeline + Vercel Edge Web Portal with Recharts interactive UI."
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

        tb = s6.shapes.add_textbox(qx + Inches(0.25), qy + Inches(0.18), qw - Inches(0.5), qh - Inches(0.36))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        h = tf.paragraphs[0]
        h.text = q_title
        h.font.name = "Arial"
        h.font.size = Pt(12.5)
        h.font.bold = True
        h.font.color.rgb = q_theme_color if q_theme_color != RGBColor(37, 99, 235) else RGBColor(29, 78, 216)
        h.alignment = PP_ALIGN.CENTER
        h.space_after = Pt(8)

        for item in q_items:
            p = tf.add_paragraph()
            p.space_after = Pt(4)
            r = p.add_run()
            r.text = "• " + item
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            r.font.color.rgb = C_TEXT_MAIN

    prs.save(output_path)
    print(f"Successfully generated highly visual presentation at {output_path}")

if __name__ == "__main__":
    out_file = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24\scratch\AirIntel_India_SIH26056_Presentation.pptx"
    create_reviewed_presentation(out_file)
