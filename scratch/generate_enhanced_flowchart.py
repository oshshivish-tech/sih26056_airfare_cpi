import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_enhanced_architecture_diagram(output_path):
    # Proportions: 14.5 width x 10.5 height, rendered at 300 DPI for ultra sharpness
    fig, ax = plt.subplots(figsize=(14.5, 10.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    navy_dark = '#0f172a'
    slate_desc = '#1e293b' # Very dark, high-contrast text
    
    stages = [
        {
            "id": 1,
            "title": "TIER 1: HARVESTING",
            "subtitle": "Distributed Web Extraction",
            "color_top": "#1d4ed8",      # Royal Blue
            "color_light": "#eff6ff",    # Light Blue
            "color_border": "#3b82f6",
            "x": 1.5, "y": 2.5, "w": 22.0, "h": 95,
            "badge": "⏱️  02:00 AM IST DAILY CRON",
            "items": [
                ("🌐 Direct Portals", "IndiGo, Air India, Akasa, SpiceJet"),
                ("🕷️ Stealth Engine", "Playwright headless + stealth pool"),
                ("📅 5 Horizons", "T+1, T+7, T+15, T+30, T+45 days"),
                ("🛡️ Ethical Scrape", "Strict robots.txt rate-limiting")
            ]
        },
        {
            "id": 2,
            "title": "TIER 2: CLEANSING",
            "subtitle": "Normalization & Outliers",
            "color_top": "#059669",      # Emerald Green
            "color_light": "#f0fdf4",    # Light Green
            "color_border": "#10b981",
            "x": 26.2, "y": 2.5, "w": 22.0, "h": 95,
            "badge": "📊  IQR DYNAMIC FILTER",
            "items": [
                ("💰 Fare Isolator", "Strips GST, UDF & ancillary fees"),
                ("📋 Normalization", "Corridor, flight ID, date schema"),
                ("✂️ Dynamic IQR", "Automated Z-score outlier filter"),
                ("🧹 Phantom Scrub", "Purges cache glitches & stale fares")
            ]
        },
        {
            "id": 3,
            "title": "TIER 3: INDEX ENGINE",
            "subtitle": "UN/ILO Statistical Math",
            "color_top": "#d97706",      # Amber / Gold
            "color_light": "#fffbeb",    # Light Amber
            "color_border": "#f59e0b",
            "x": 50.9, "y": 2.5, "w": 22.0, "h": 95,
            "badge": "📐  UN/ILO CHAPTER 10",
            "items": [
                ("🧮 Jevons GM", "I_J = ∏(p_t / p_0)^(1/n) formula"),
                ("⚖️ Zero Bias", "Eliminates Dutot upward distortion"),
                ("✈️ DGCA Weights", "Calibrated by passenger volume"),
                ("📈 Laspeyres", "Composite 12 metro corridors index")
            ]
        },
        {
            "id": 4,
            "title": "TIER 4: VAULT & API",
            "subtitle": "Cryptographic Audit & API",
            "color_top": "#7c3aed",      # Deep Purple
            "color_light": "#faf5ff",    # Light Purple
            "color_border": "#8b5cf6",
            "x": 75.6, "y": 2.5, "w": 22.8, "h": 95,
            "badge": "🔒  SHA-256 PROVENANCE",
            "items": [
                ("🔐 SHA-256 Vault", "Immutable Merkle batch digests"),
                ("🗄️ PostgreSQL", "NDSAP sovereign legal audit ledger"),
                ("⚡ FastAPI Feed", "Real-time /api/v1/apix/* REST"),
                ("🏛️ MoSPI Portal", "eSankhyiki CSV & React 19 UI")
            ]
        }
    ]

    for st in stages:
        # Outer Card Container with clean shadow appearance
        shadow_rect = patches.FancyBboxPatch(
            (st["x"] + 0.3, st["y"] - 0.5), st["w"], st["h"],
            boxstyle="round,pad=0.2,rounding_size=2.0",
            edgecolor="none", facecolor="#e2e8f0",
            zorder=1
        )
        ax.add_patch(shadow_rect)

        rect = patches.FancyBboxPatch(
            (st["x"], st["y"]), st["w"], st["h"],
            boxstyle="round,pad=0.2,rounding_size=2.0",
            edgecolor=st["color_border"], facecolor="#ffffff",
            linewidth=2.0, zorder=2
        )
        ax.add_patch(rect)

        # Header Banner
        header_h = 16.5
        header_rect = patches.FancyBboxPatch(
            (st["x"], st["y"] + st["h"] - header_h), st["w"], header_h,
            boxstyle="round,pad=0.1,rounding_size=1.6",
            edgecolor="none", facecolor=st["color_top"],
            zorder=3
        )
        ax.add_patch(header_rect)

        # Header Title
        ax.text(
            st["x"] + st["w"]/2, st["y"] + st["h"] - 6.0,
            st["title"],
            color="#ffffff", fontsize=13.0, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="Arial"
        )
        # Header Subtitle
        ax.text(
            st["x"] + st["w"]/2, st["y"] + st["h"] - 11.8,
            st["subtitle"],
            color="#f8fafc",
            fontsize=10.0, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="Arial"
        )

        # Stage Metric / Trigger Pill Badge
        badge_y = st["y"] + st["h"] - header_h - 6.0
        badge_rect = patches.FancyBboxPatch(
            (st["x"] + 1.2, badge_y), st["w"] - 2.4, 4.8,
            boxstyle="round,pad=0.1,rounding_size=1.2",
            edgecolor=st["color_border"], facecolor=st["color_light"],
            linewidth=1.4, zorder=3
        )
        ax.add_patch(badge_rect)
        ax.text(
            st["x"] + st["w"]/2, badge_y + 2.4,
            st["badge"],
            color=st["color_top"], fontsize=9.2, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="Arial"
        )

        # 4 High-Density Process Item Cards
        start_y = st["y"] + st["h"] - header_h - 13.0
        card_h = 15.0
        card_spacing = 17.5

        for idx, (head, desc) in enumerate(st["items"]):
            item_y = start_y - (idx * card_spacing)
            
            # Item Box with accent left border
            item_box = patches.FancyBboxPatch(
                (st["x"] + 1.2, item_y - card_h), st["w"] - 2.4, card_h,
                boxstyle="round,pad=0.2,rounding_size=1.2",
                edgecolor=st["color_border"], facecolor=st["color_light"],
                linewidth=1.2, zorder=3
            )
            ax.add_patch(item_box)

            # Left Color Accent Pill inside the card
            accent_pill = patches.Rectangle(
                (st["x"] + 1.3, item_y - card_h + 0.3), 0.7, card_h - 0.6,
                facecolor=st["color_top"], edgecolor="none", zorder=4
            )
            ax.add_patch(accent_pill)

            # Item Head (Large, Bold, High-Contrast)
            ax.text(
                st["x"] + 2.8, item_y - 4.2,
                head,
                color=navy_dark, fontsize=11.2, fontweight="bold",
                ha="left", va="center", zorder=5, fontfamily="Arial"
            )
            # Item Desc (Readable, Crisp Dark Slate)
            ax.text(
                st["x"] + 2.8, item_y - 10.2,
                desc,
                color=slate_desc, fontsize=9.6, fontweight="normal",
                ha="left", va="center", zorder=5, fontfamily="Arial"
            )

    # Connecting Flow Arrows between stages
    arrow_positions = [
        (23.5, 48.0),
        (48.2, 48.0),
        (72.9, 48.0)
    ]
    for ax_pos, ay_pos in arrow_positions:
        # Arrow circular backdrop
        arrow_circle = patches.Circle(
            (ax_pos + 1.35, ay_pos), 2.2,
            facecolor="#eff6ff", edgecolor="#3b82f6", linewidth=1.5, zorder=8
        )
        ax.add_patch(arrow_circle)

        ax.text(
            ax_pos + 1.35, ay_pos, "➔",
            color="#1d4ed8", fontsize=18, fontweight="black",
            ha="center", va="center", zorder=10
        )

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Successfully generated enhanced architecture diagram at {output_path}")

if __name__ == "__main__":
    out_file = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\architecture_diagram.png"
    create_enhanced_architecture_diagram(out_file)
