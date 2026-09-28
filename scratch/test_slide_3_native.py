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
    s3 = prs.slides.add_slide(blank_layout)

    C_WHITE = RGBColor(255, 255, 255)
    C_BLACK = RGBColor(0, 0, 0)
    C_NAVY = RGBColor(27, 54, 93)
    C_BLUE_TEMPLATE = RGBColor(30, 64, 175)
    C_RED_TEMPLATE = RGBColor(220, 38, 38)
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(71, 85, 105)

    # Background
    bg = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_WHITE
    bg.line.fill.background()

    # Team Rookie Pill
    pill = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(0.22), Inches(1.8), Inches(0.55))
    pill.adjustments[0] = 0.5
    pill.fill.solid()
    pill.fill.fore_color.rgb = C_WHITE
    pill.line.color.rgb = RGBColor(100, 116, 139)
    pill.line.width = Pt(1.5)
    p_p = pill.text_frame.paragraphs[0]
    p_p.text = "Team Rookie"
    p_p.font.name = "Arial"
    p_p.font.size = Pt(13)
    p_p.font.bold = True
    p_p.font.color.rgb = C_BLACK
    p_p.alignment = PP_ALIGN.CENTER

    # Title
    tb_t = s3.shapes.add_textbox(Inches(2.5), Inches(0.18), Inches(8.3), Inches(0.85))
    p_t = tb_t.text_frame.paragraphs[0]
    p_t.text = "TECHNICAL APPROACH"
    p_t.font.name = "Times New Roman"
    p_t.font.size = Pt(25)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY
    p_t.alignment = PP_ALIGN.CENTER

    # SIH Logo
    sih_top_logo = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\page_1_img_2.png"
    if os.path.exists(sih_top_logo):
        s3.shapes.add_picture(sih_top_logo, Inches(11.1), Inches(0.12), Inches(1.8), Inches(0.85))

    col_y = Inches(1.15)
    col_h = Inches(5.95)

    # 1. Left Box: Technologies Used (Width = 4.3 inches)
    col_left_w = Inches(4.30)
    box_left = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), col_y, col_left_w, col_h)
    box_left.fill.solid()
    box_left.fill.fore_color.rgb = C_WHITE
    box_left.line.color.rgb = C_BLUE_TEMPLATE
    box_left.line.width = Pt(1.5)

    tb_l = s3.shapes.add_textbox(Inches(0.72), col_y + Inches(0.15), col_left_w - Inches(0.34), col_h - Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p_th = tf_l.paragraphs[0]
    p_th.text = "Technologies Used:"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(17)
    p_th.font.bold = True
    p_th.font.color.rgb = C_BLUE_TEMPLATE
    p_th.space_after = Pt(10)

    p_lh = tf_l.add_paragraph()
    r_lh = p_lh.add_run()
    r_lh.text = "Languages: "
    r_lh.font.name = "Arial"
    r_lh.font.size = Pt(14)
    r_lh.font.bold = True
    r_lh.font.color.rgb = C_RED_TEMPLATE

    r_lv = p_lh.add_run()
    r_lv.text = "Python 3.13 (Crawlers & Engine), TypeScript (Dashboard), SQL (Storage)."
    r_lv.font.name = "Arial"
    r_lv.font.size = Pt(12.5)
    r_lv.font.bold = True
    r_lv.font.color.rgb = C_BLACK
    p_lh.space_after = Pt(12)

    p_tfh = tf_l.add_paragraph()
    p_tfh.text = "Tools & Frameworks:"
    p_tfh.font.name = "Arial"
    p_tfh.font.size = Pt(14)
    p_tfh.font.bold = True
    p_tfh.font.color.rgb = C_RED_TEMPLATE
    p_tfh.space_after = Pt(6)

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

    for tool in tools_list:
        pt = tf_l.add_paragraph()
        pt.space_after = Pt(5)
        r = pt.add_run()
        r.text = "• " + tool
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = C_BLACK

    # 2. Right Section: Architecture Flowchart (4 Tiers)
    flow_x_start = Inches(5.02)
    flow_w_total = Inches(7.76)
    col_w = Inches(1.81)
    gap_w = Inches(0.17)

    tier_data = [
        (
            "TIER 1: HARVESTING", "Distributed Web Extraction",
            "⏱️ 02:00 AM IST CRON",
            RGBColor(37, 99, 235), RGBColor(239, 246, 255),
            [
                ("🌐 Direct Portals", "Live scrape: IndiGo, Air India, Akasa, SpiceJet", "Zero API costs via direct endpoints"),
                ("🕷️ Stealth Engine", "Playwright headless + stealth proxy pool", "Evades anti-bot & Cloudflare blocks"),
                ("📅 5 Horizons", "T+1, T+7, T+15, T+30, T+45 advance curves", "Captures full dynamic yield trajectory"),
                ("🛡️ Ethical Scrape", "Strict robots.txt rate-limiting adherence", "Off-peak nightly execution batches")
            ]
        ),
        (
            "TIER 2: CLEANSING", "Normalization & Outliers",
            "📊 IQR DYNAMIC FILTER",
            RGBColor(5, 150, 105), RGBColor(240, 253, 244),
            [
                ("💰 Fare Isolator", "Strips GST, UDF & ancillary fees", "Extracts pure base fare + fuel charge"),
                ("📋 Schema Norm", "Unifies route, flight ID, date & cabin tier", "Consistent relational JSON schema"),
                ("✂️ Dynamic IQR", "Interquartile outlier filter removes flash spikes", "Truncates unrepresentative ±1.5 IQR"),
                ("🧹 Phantom Scrub", "Purges cache glitches & stale inventory", "Validates seat availability in real time")
            ]
        ),
        (
            "TIER 3: INDEX ENGINE", "UN/ILO Statistical Math",
            "📐 UN/ILO CHAPTER 10",
            RGBColor(217, 119, 6), RGBColor(254, 252, 232),
            [
                ("🧮 Jevons GM", "I_J = ∏(p_t / p_0)^(1/n) geometric mean", "Elementary unweighted price relative"),
                ("⚖️ Zero Bias", "Eliminates Dutot upward substitution distortion", "UN/ILO Chapter 10 axiomatic compliance"),
                ("✈️ DGCA Weights", "Calibrated by monthly route passenger volume", "Accurately reflects real consumer share"),
                ("📈 Laspeyres", "Aggregates 12 metro corridors composite index", "Produces headline inflation relative")
            ]
        ),
        (
            "TIER 4: VAULT & API", "Cryptographic Audit & API",
            "🔒 SHA-256 PROVENANCE",
            RGBColor(124, 58, 237), RGBColor(250, 245, 255),
            [
                ("🔐 SHA-256 Vault", "Immutable Merkle batch audit fingerprints", "Sovereign-grade judicial auditability"),
                ("🗄️ PostgreSQL", "NDSAP-compliant sovereign relational store", "Partitioned time-series historical DB"),
                ("⚡ FastAPI Feed", "High-throughput REST API (/api/v1/apix/*)", "Sub-10ms response with OpenAPI 3.1"),
                ("🏛️ MoSPI Portal", "Direct eSankhyiki CSV & live React 19 UI", "Real-time feed for RBI policy setting")
            ]
        )
    ]

    for t_idx, (t_title, t_sub, t_badge, theme_col, bg_col, cards) in enumerate(tier_data):
        cx = flow_x_start + t_idx * (col_w + gap_w)

        # Outer Container Box
        c_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, col_y, col_w, col_h)
        c_box.adjustments[0] = 0.04
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = C_WHITE
        c_box.line.color.rgb = theme_col
        c_box.line.width = Pt(1.5)

        # Header Box
        h_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, col_y, col_w, Inches(0.92))
        h_box.adjustments[0] = 0.15
        h_box.fill.solid()
        h_box.fill.fore_color.rgb = theme_col
        h_box.line.fill.background()

        tf_h = h_box.text_frame
        tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0
        p_th1 = tf_h.paragraphs[0]
        p_th1.text = t_title
        p_th1.font.name = "Arial"
        p_th1.font.size = Pt(9.8)
        p_th1.font.bold = True
        p_th1.font.color.rgb = C_WHITE
        p_th1.alignment = PP_ALIGN.CENTER

        p_th2 = tf_h.add_paragraph()
        p_th2.text = t_sub
        p_th2.font.name = "Arial"
        p_th2.font.size = Pt(8.0)
        p_th2.font.bold = True
        p_th2.font.color.rgb = RGBColor(241, 245, 249)
        p_th2.alignment = PP_ALIGN.CENTER

        # Badge Pill
        b_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.08), col_y + Inches(1.00), col_w - Inches(0.16), Inches(0.34))
        b_box.adjustments[0] = 0.4
        b_box.fill.solid()
        b_box.fill.fore_color.rgb = bg_col
        b_box.line.color.rgb = theme_col
        b_box.line.width = Pt(1.0)

        tf_b = b_box.text_frame
        tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.text = t_badge
        p_b.font.name = "Arial"
        p_b.font.size = Pt(7.8)
        p_b.font.bold = True
        p_b.font.color.rgb = theme_col
        p_b.alignment = PP_ALIGN.CENTER

        # 4 Stacked Process Cards (nicely filling the column height)
        card_start_y = col_y + Inches(1.42)
        card_h = Inches(1.04)
        card_gap = Inches(0.08)

        for c_idx, (c_head, c_desc1, c_desc2) in enumerate(cards):
            card_y = card_start_y + c_idx * (card_h + card_gap)
            cd_shape = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.07), card_y, col_w - Inches(0.14), card_h)
            cd_shape.adjustments[0] = 0.1
            cd_shape.fill.solid()
            cd_shape.fill.fore_color.rgb = bg_col
            cd_shape.line.color.rgb = theme_col
            cd_shape.line.width = Pt(1.0)

            tb_cd = s3.shapes.add_textbox(cx + Inches(0.11), card_y + Inches(0.05), col_w - Inches(0.22), card_h - Inches(0.10))
            tf_cd = tb_cd.text_frame
            tf_cd.word_wrap = True
            tf_cd.margin_left = tf_cd.margin_right = tf_cd.margin_top = tf_cd.margin_bottom = 0

            p_cd1 = tf_cd.paragraphs[0]
            p_cd1.text = c_head
            p_cd1.font.name = "Arial"
            p_cd1.font.size = Pt(8.8)
            p_cd1.font.bold = True
            p_cd1.font.color.rgb = theme_col

            p_cd2 = tf_cd.add_paragraph()
            p_cd2.text = c_desc1
            p_cd2.font.name = "Arial"
            p_cd2.font.size = Pt(7.4)
            p_cd2.font.bold = True
            p_cd2.font.color.rgb = C_TEXT_DARK

            p_cd3 = tf_cd.add_paragraph()
            p_cd3.text = c_desc2
            p_cd3.font.name = "Arial"
            p_cd3.font.size = Pt(7.0)
            p_cd3.font.color.rgb = C_TEXT_MUTED

        # Right-pointing Arrow Shape between columns
        if t_idx < 3:
            arrow_x = cx + col_w + Inches(0.02)
            arrow_shape = s3.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, col_y + Inches(3.85), gap_w - Inches(0.04), Inches(0.26))
            arrow_shape.fill.solid()
            arrow_shape.fill.fore_color.rgb = RGBColor(37, 99, 235)
            arrow_shape.line.fill.background()

    out_test = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\scratch\test_slide_3.pptx"
    prs.save(out_test)
    print(f"Saved test slide 3 to {out_test}")

if __name__ == "__main__":
    test_slide_3()
