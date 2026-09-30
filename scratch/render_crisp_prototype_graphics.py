import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np

base_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
pres_dir = os.path.join(base_dir, "public", "presentation")
os.makedirs(pres_dir, exist_ok=True)

def render_prototype_chart():
    fig, ax = plt.subplots(figsize=(10.5, 4.4), dpi=200)
    fig.patch.set_facecolor('#0B132B') # Dark navy theme matching prototype dashboard
    ax.set_facecolor('#0F172A')

    months = ['Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26 (Live)']
    x = np.arange(len(months))

    jevons = [100.0, 102.3, 114.5, 106.8, 103.4, 105.1, 108.9, 118.2, 112.6, 107.4, 109.8, 111.4]
    dutot =  [100.0, 102.8, 116.2, 107.5, 104.1, 105.8, 109.8, 120.4, 113.9, 108.1, 110.6, 112.5]
    weighted = [100.0, 102.1, 115.2, 106.2, 103.1, 104.9, 108.5, 117.8, 112.1, 107.0, 109.4, 111.0]
    mospi =  [100.0, 101.8, 112.5, 105.4, 102.9, 104.2, 107.6, 115.0, 110.8, 106.5, 108.2, 109.5]

    # Grid
    ax.grid(True, linestyle='--', color='#334155', alpha=0.5, zorder=0)

    # Base line
    ax.axhline(100.0, color='#64748B', linestyle=':', linewidth=1.2, label='Base Period = 100.0', zorder=1)

    # Lines
    ax.plot(x, jevons, color='#38BDF8', linewidth=2.8, marker='o', markersize=4.5, label='Jevons Index (Geometric) — 111.4', zorder=5)
    ax.plot(x, weighted, color='#34D399', linewidth=2.2, linestyle='--', marker='s', markersize=4, label='DGCA Weighted Laspeyres — 111.0', zorder=4)
    ax.plot(x, mospi, color='#C084FC', linewidth=2.0, linestyle='-.', marker='^', markersize=4, label='Official MoSPI CPI Baseline — 109.5', zorder=3)
    ax.plot(x, dutot, color='#FBBF24', linewidth=1.8, linestyle=':', marker='d', markersize=3.5, label='Arithmetic-mean (Dutot) benchmark* — 112.5', zorder=2)

    # Highlight latest live point
    ax.scatter([x[-1]], [jevons[-1]], color='#38BDF8', s=90, edgecolors='#FFFFFF', linewidth=1.5, zorder=6)
    ax.annotate('Live: 111.4', xy=(x[-1], jevons[-1]), xytext=(x[-1]-1.2, jevons[-1]+3.2),
                fontsize=9.5, fontweight='bold', color='#38BDF8',
                arrowprops=dict(arrowstyle='->', color='#38BDF8', lw=1.2))

    # Ticks & labels
    ax.set_xticks(x)
    ax.set_xticklabels(months, fontsize=8.5, color='#94A3B8', rotation=15)
    ax.set_yticks(np.arange(90, 131, 5))
    ax.set_yticklabels([str(y) for y in np.arange(90, 131, 5)], fontsize=9, color='#94A3B8')
    ax.set_ylim(92, 126)
    ax.set_ylabel('Index Value (Oct 2025 = 100.0)', fontsize=9.5, color='#E2E8F0', fontweight='bold')

    # Spines
    for spine in ax.spines.values():
        spine.set_color('#334155')

    # Legend
    leg = ax.legend(loc='upper left', fontsize=8, facecolor='#0F172A', edgecolor='#334155', labelcolor='#E2E8F0', framealpha=0.95)

    # Prototype Data: Sample Badge
    bbox_props = dict(boxstyle="round,pad=0.3", fc="#FEF3C7", ec="#F59E0B", lw=1.2)
    ax.text(0.985, 0.94, "Prototype data: sample", transform=ax.transAxes, fontsize=8.5,
            fontweight='bold', color='#92400E', ha='right', va='top', bbox=bbox_props)

    # Footnote
    fig.text(0.12, 0.02, "* Footnote: Arithmetic-mean (Dutot) benchmark is an unweighted arithmetic series demonstrating upward substitution bias; NOT an official MoSPI series.",
             fontsize=7.2, color='#94A3B8', style='italic')

    plt.tight_layout(rect=[0, 0.05, 1, 0.98])
    chart_path = os.path.join(pres_dir, "vayusuchak_prototype_chart.png")
    fig.savefig(chart_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"Generated {chart_path}")

def render_corridor_table():
    width = 1600
    height = 840
    img = Image.new('RGB', (width, height), color='#0c1322')
    draw = ImageDraw.Draw(img)

    # Fonts
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 28)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
    font_th = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 18)
    font_td_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 19)
    font_td_regular = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
    font_mono = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 17)

    # Title
    title_text = "Corridor-Wise Yield & Weight Matrix (12 Representative Domestic Sectors)"
    draw.text((45, 26), title_text, fill='#ffffff', font=font_title)

    # Prototype Data: Sample Badge
    badge_text = "Prototype data: sample"
    bbox_b = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bbox_b[2] - bbox_b[0] + 24
    bh = bbox_b[3] - bbox_b[1] + 10
    bx = width - 45 - bw
    by = 28
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=8, fill='#fef3c7', outline='#f59e0b', width=1)
    draw.text((bx + 12, by + 4), badge_text, fill='#92400e', font=font_badge)

    # Table dimensions
    tbl_x = 45
    tbl_y = 80
    tbl_w = width - 90
    tbl_h = height - 105

    col_widths = [450, 200, 200, 220, 220, 220]
    headers = ["CORRIDOR", "CATEGORY", "RAW DGCA", "BASKET WT (w_c)", "BASE FARE", "CURRENT AVG"]
    alignments = ["left", "left", "center", "center", "center", "center"]

    rows = [
        ("Delhi ↔ Mumbai (DEL-BOM)", "METRO-METRO", "14.8%", "18.2%", "₹ 4,850", "₹ 5,420 (+11.8%)"),
        ("Bengaluru ↔ Delhi (BLR-DEL)", "METRO-METRO", "11.0%", "13.5%", "₹ 5,120", "₹ 5,690 (+11.1%)"),
        ("Mumbai ↔ Bengaluru (BOM-BLR)", "METRO-METRO", "9.8%", "12.0%", "₹ 3,950", "₹ 4,390 (+11.1%)"),
        ("Kolkata ↔ Delhi (CCU-DEL)", "METRO-METRO", "7.9%", "9.7%", "₹ 5,400", "₹ 6,020 (+11.5%)"),
        ("Hyderabad ↔ Delhi (HYD-DEL)", "METRO-METRO", "7.4%", "9.1%", "₹ 4,680", "₹ 5,190 (+10.9%)"),
        ("Chennai ↔ Delhi (MAA-DEL)", "METRO-METRO", "6.5%", "8.0%", "₹ 5,290", "₹ 5,880 (+11.2%)"),
        ("Delhi ↔ Pune (DEL-PNQ)", "METRO-TIER2", "5.7%", "7.0%", "₹ 4,410", "₹ 4,920 (+11.6%)"),
        ("Delhi ↔ Ahmedabad (DEL-AMD)", "METRO-TIER2", "5.1%", "6.3%", "₹ 3,820", "₹ 4,240 (+11.0%)"),
        ("Delhi ↔ Guwahati (DEL-GAU)", "METRO-TIER2", "4.0%", "4.9%", "₹ 6,150", "₹ 6,650 (+8.1%)"),
    ]

    header_h = 56
    row_h = (tbl_h - header_h) / len(rows)

    # Outer container
    draw.rectangle([tbl_x, tbl_y, tbl_x + tbl_w, tbl_y + tbl_h], fill='#0f172a', outline='#1e293b', width=2)
    draw.rectangle([tbl_x, tbl_y, tbl_x + tbl_w, tbl_y + header_h], fill='#1e293b')

    # Column dividers
    cur_x = tbl_x
    for w in col_widths[:-1]:
        cur_x += w
        draw.line([(cur_x, tbl_y), (cur_x, tbl_y + tbl_h)], fill='#1e293b', width=1)

    # Headers
    cur_x = tbl_x
    for i, h_text in enumerate(headers):
        w = col_widths[i]
        align = alignments[i]
        bbox = draw.textbbox((0, 0), h_text, font=font_th)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        y_pos = tbl_y + (header_h - th) // 2 - 2

        if align == "left":
            x_pos = cur_x + 20
        elif align == "center":
            x_pos = cur_x + (w - tw) // 2
        else:
            x_pos = cur_x + w - tw - 20

        draw.text((x_pos, y_pos), h_text, fill='#94a3b8', font=font_th)
        cur_x += w

    draw.line([(tbl_x, tbl_y + header_h), (tbl_x + tbl_w, tbl_y + header_h)], fill='#334155', width=1)

    # Rows
    for r_idx, row in enumerate(rows):
        ry = tbl_y + header_h + int(r_idx * row_h)
        if r_idx % 2 == 1:
            draw.rectangle([tbl_x + 1, ry + 1, tbl_x + tbl_w - 1, ry + int(row_h) - 1], fill='#131e33')

        if r_idx > 0:
            draw.line([(tbl_x, ry), (tbl_x + tbl_w, ry)], fill='#1e293b', width=1)

        cur_x = tbl_x
        for c_idx, cell_value in enumerate(row):
            w = col_widths[c_idx]
            align = alignments[c_idx]
            font_to_use = font_td_bold if c_idx in [0, 3] else font_td_regular

            # Text color
            if c_idx == 0:
                color = '#ffffff'
            elif c_idx == 1:
                color = '#38bdf8' if 'METRO-METRO' in cell_value else '#c084fc'
            elif c_idx == 2:
                color = '#94a3b8'
            elif c_idx == 3:
                color = '#34d399' # Normalized basket weight highlighted in emerald
            elif c_idx == 4:
                color = '#cbd5e1'
            else:
                color = '#f59e0b'

            bbox = draw.textbbox((0, 0), cell_value, font=font_to_use)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            y_pos = ry + (int(row_h) - th) // 2 - 2

            if align == "left":
                x_pos = cur_x + 20
            elif align == "center":
                x_pos = cur_x + (w - tw) // 2
            else:
                x_pos = cur_x + w - tw - 20

            draw.text((x_pos, y_pos), cell_value, fill=color, font=font_to_use)
            cur_x += w

    table_path = os.path.join(pres_dir, "vayusuchak_prototype_table.png")
    img.save(table_path)
    print(f"Generated {table_path}")

if __name__ == "__main__":
    render_prototype_chart()
    render_corridor_table()
