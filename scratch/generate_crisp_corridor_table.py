import os
from PIL import Image, ImageDraw, ImageFont

def render_corridor_table():
    width = 1600
    height = 840
    img = Image.new('RGB', (width, height), color='#0c1322')
    draw = ImageDraw.Draw(img)

    # Fonts
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 30)
    font_th = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 18)
    font_td_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
    font_td_regular = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 19)

    # Title
    title_text = "Corridor-Wise Average Fare & Weight Table (Top Indian Domestic Sectors)"
    draw.text((45, 30), title_text, fill='#ffffff', font=font_title)

    # Table dimensions
    tbl_x = 45
    tbl_y = 85
    tbl_w = width - 90
    tbl_h = height - 115

    # Columns configuration
    # Total width = 1510
    # Columns:
    # 0: Corridor (520px)
    # 1: Category (230px)
    # 2: DGCA Weight (190px)
    # 3: Base Fare (190px)
    # 4: Current Avg (190px)
    # 5: Inflation (190px)
    # 520 + 230 + 190*4 = 750 + 760 = 1510! Perfect match!
    col_widths = [520, 230, 190, 190, 190, 190]
    headers = ["CORRIDOR", "CATEGORY", "DGCA WEIGHT", "BASE FARE", "CURRENT AVG", "INFLATION"]
    alignments = ["left", "left", "center", "center", "center", "center"]

    rows = [
        ("DEL - BOM (Delhi - Mumbai)", "METRO-METRO", "18.5%", "₹ 4,850", "₹ 5,534", "+14.1%"),
        ("BOM - BLR (Mumbai - Bengaluru)", "METRO-METRO", "11.2%", "₹ 3,950", "₹ 4,424", "+12.0%"),
        ("DEL - BLR (Delhi - Bengaluru)", "METRO-METRO", "10.8%", "₹ 5,120", "₹ 5,734", "+12.0%"),
        ("CCU - DEL (Kolkata - Delhi)", "METRO-METRO", "7.9%", "₹ 5,400", "₹ 6,129", "+13.5%"),
        ("HYD - DEL (Hyderabad - Delhi)", "METRO-METRO", "7.4%", "₹ 4,680", "₹ 5,242", "+12.0%"),
        ("MAA - DEL (Chennai - Delhi)", "METRO-METRO", "6.5%", "₹ 5,290", "₹ 5,935", "+12.2%"),
        ("DEL - PNQ (Delhi - Pune)", "METRO-TIER2", "5.7%", "₹ 4,410", "₹ 4,939", "+12.0%"),
        ("DEL - AMD (Delhi - Ahmedabad)", "METRO-TIER2", "5.1%", "₹ 3,820", "₹ 4,278", "+12.0%"),
        ("DEL - GAU (Delhi - Guwahati)", "METRO-TIER2", "4.0%", "₹ 6,150", "₹ 6,531", "+6.2%"),
    ]

    header_h = 58
    row_h = (tbl_h - header_h) / len(rows)

    # Draw outer container border & background
    draw.rectangle([tbl_x, tbl_y, tbl_x + tbl_w, tbl_y + tbl_h], fill='#0f172a', outline='#1e293b', width=2)

    # Draw header background
    draw.rectangle([tbl_x, tbl_y, tbl_x + tbl_w, tbl_y + header_h], fill='#1e293b')

    # Draw vertical column dividers
    cur_x = tbl_x
    for w in col_widths[:-1]:
        cur_x += w
        draw.line([(cur_x, tbl_y), (cur_x, tbl_y + tbl_h)], fill='#1e293b', width=1)

    # Draw header text
    cur_x = tbl_x
    for i, h_text in enumerate(headers):
        w = col_widths[i]
        align = alignments[i]
        bbox = draw.textbbox((0, 0), h_text, font=font_th)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        y_pos = tbl_y + (header_h - th) // 2 - 2

        if align == "left":
            x_pos = cur_x + 24
        elif align == "center":
            x_pos = cur_x + (w - tw) // 2
        else:
            x_pos = cur_x + w - tw - 24

        draw.text((x_pos, y_pos), h_text, fill='#94a3b8', font=font_th)
        cur_x += w

    # Draw header bottom line
    draw.line([(tbl_x, tbl_y + header_h), (tbl_x + tbl_w, tbl_y + header_h)], fill='#334155', width=1)

    # Draw rows
    for r_idx, row in enumerate(rows):
        ry = tbl_y + header_h + int(r_idx * row_h)
        # Alternate subtle row background
        if r_idx % 2 == 1:
            draw.rectangle([tbl_x + 1, ry + 1, tbl_x + tbl_w - 1, ry + int(row_h) - 1], fill='#131e33')

        # Horizontal row divider
        if r_idx > 0:
            draw.line([(tbl_x, ry), (tbl_x + tbl_w, ry)], fill='#1e293b', width=1)

        # Columns
        cur_x = tbl_x
        for c_idx, val in enumerate(row):
            w = col_widths[c_idx]
            align = alignments[c_idx]

            # Choose font and color
            if c_idx == 0:
                font = font_td_bold
                color = '#ffffff'
            elif c_idx == 1:
                font = font_td_regular
                color = '#cbd5e1'
            elif c_idx == 2:
                font = font_td_bold
                color = '#38bdf8' # Bright Sky Blue
            elif c_idx in (3, 4):
                font = font_td_regular
                color = '#f1f5f9'
            else: # c_idx == 5 (Inflation)
                font = font_td_bold
                color = '#f87171' # Crisp Red-Pink Inflation

            bbox = draw.textbbox((0, 0), val, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            y_pos = ry + (int(row_h) - th) // 2 - 2

            if align == "left":
                x_pos = cur_x + 24
            elif align == "center":
                x_pos = cur_x + (w - tw) // 2
            else:
                x_pos = cur_x + w - tw - 24

            draw.text((x_pos, y_pos), val, fill=color, font=font)
            cur_x += w

    # Save to public and dist directories
    out_paths = [
        r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\vayusuchak_prototype_table.png",
        r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\dist\presentation\vayusuchak_prototype_table.png",
        r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\scratch\test_crisp_table.png"
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        img.save(p, "PNG")
    print("Successfully generated crisp prototype table at all paths!")

if __name__ == '__main__':
    render_corridor_table()
