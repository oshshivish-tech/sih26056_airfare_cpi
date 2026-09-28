import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_system_architecture_diagram(output_path):
    fig, ax = plt.subplots(figsize=(13.5, 7.0), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    navy_dark = '#0f172a'
    slate_border = '#cbd5e1'
    
    stages = [
        {
            "id": 1,
            "title": "TIER 1: HARVESTING",
            "subtitle": "Distributed Web Extraction",
            "color_top": "#1d4ed8",
            "color_bg": "#f8fafc",
            "color_border": "#93c5fd",
            "x": 2.0, "y": 3, "w": 21.8, "h": 93,
            "badge": "02:00 AM IST CRON",
            "items": [
                ("Direct Airline Portals", "IndiGo, Air India, Akasa, SpiceJet"),
                ("Stealth Crawler Engine", "Playwright headless + Proxy pool"),
                ("5 Forward Horizons", "T+1, T+7, T+15, T+30, T+45 days"),
                ("Ethical Adherence", "Strict robots.txt rate-limiting")
            ]
        },
        {
            "id": 2,
            "title": "TIER 2: CLEANSING",
            "subtitle": "Normalization & Outliers",
            "color_top": "#047857",
            "color_bg": "#f8fafc",
            "color_border": "#86efac",
            "x": 26.8, "y": 3, "w": 21.8, "h": 93,
            "badge": "IQR DYNAMIC FILTER",
            "items": [
                ("Base Fare Pure Isolator", "Strips GST, UDF, and ancillary fees"),
                ("Schema Normalization", "Corridor, flight ID, departure date"),
                ("Dynamic IQR Truncation", "Automated Z-score outlier filtering"),
                ("Phantom Fare Scrub", "Eliminates cache glitches & scrap errors")
            ]
        },
        {
            "id": 3,
            "title": "TIER 3: INDEX ENGINE",
            "subtitle": "UN/ILO Statistical Math",
            "color_top": "#b45309",
            "color_bg": "#f8fafc",
            "color_border": "#fde68a",
            "x": 51.6, "y": 3, "w": 21.8, "h": 93,
            "badge": "UN/ILO CHAPTER 10",
            "items": [
                ("UN/ILO Jevons GM", "I_J = ∏ (pt / p0)^(1/n) formula"),
                ("Zero Substitution Bias", "Eliminates Dutot upward distortion"),
                ("DGCA Traffic Weights", "Calibrated by passenger volume"),
                ("Laspeyres Aggregator", "Composite 12 metro corridors index")
            ]
        },
        {
            "id": 4,
            "title": "TIER 4: VAULT & API",
            "subtitle": "Cryptographic Audit & API",
            "color_top": "#6d28d9",
            "color_bg": "#f8fafc",
            "color_border": "#c4b5fd",
            "x": 76.4, "y": 3, "w": 22.2, "h": 93,
            "badge": "SHA-256 PROVENANCE",
            "items": [
                ("SHA-256 Hash Vault", "Immutable Merkle batch fingerprints"),
                ("PostgreSQL Storage", "NDSAP compliant legal audit ledger"),
                ("FastAPI Microservices", "Real-time /api/v1/apix/* REST feed"),
                ("MoSPI & Web Dashboard", "eSankhyiki CSV & React 19 UI")
            ]
        }
    ]

    for st in stages:
        # Background card
        rect = patches.FancyBboxPatch(
            (st["x"], st["y"]), st["w"], st["h"],
            boxstyle="round,pad=0.5,rounding_size=2.0",
            edgecolor=st["color_border"], facecolor=st["color_bg"],
            linewidth=1.8, zorder=2
        )
        ax.add_patch(rect)

        # Header Banner
        header_h = 18.0
        header_rect = patches.FancyBboxPatch(
            (st["x"], st["y"] + st["h"] - header_h), st["w"], header_h,
            boxstyle="round,pad=0.2,rounding_size=1.5",
            edgecolor="none", facecolor=st["color_top"],
            zorder=3
        )
        ax.add_patch(header_rect)

        # Header Text
        ax.text(
            st["x"] + st["w"]/2, st["y"] + st["h"] - 7.5,
            st["title"],
            color="#ffffff", fontsize=11.5, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="sans-serif"
        )
        ax.text(
            st["x"] + st["w"]/2, st["y"] + st["h"] - 13.5,
            st["subtitle"],
            color="#e0e7ff" if "1" in st["title"] or "4" in st["title"] else "#fef08a" if "3" in st["title"] else "#d1fae5",
            fontsize=8.5, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="sans-serif"
        )

        # Stage Badge
        badge_rect = patches.FancyBboxPatch(
            (st["x"] + 2.5, st["y"] + st["h"] - header_h - 7.0), st["w"] - 5.0, 5.0,
            boxstyle="round,pad=0.2,rounding_size=1.0",
            edgecolor=st["color_top"], facecolor="#ffffff",
            linewidth=1.2, zorder=3
        )
        ax.add_patch(badge_rect)
        ax.text(
            st["x"] + st["w"]/2, st["y"] + st["h"] - header_h - 4.5,
            st["badge"],
            color=st["color_top"], fontsize=8.0, fontweight="bold",
            ha="center", va="center", zorder=4, fontfamily="sans-serif"
        )

        # Items
        start_y = st["y"] + st["h"] - header_h - 13.5
        for idx, (head, desc) in enumerate(st["items"]):
            item_y = start_y - (idx * 15.2)
            
            # Item Box
            item_box = patches.FancyBboxPatch(
                (st["x"] + 1.2, item_y - 9.5), st["w"] - 2.4, 11.8,
                boxstyle="round,pad=0.2,rounding_size=1.0",
                edgecolor=slate_border, facecolor="#ffffff",
                linewidth=0.8, zorder=3
            )
            ax.add_patch(item_box)

            # Bullet dot
            ax.plot(
                st["x"] + 2.8, item_y - 2.2,
                marker="o", markersize=5.0, color=st["color_top"], zorder=5
            )

            # Item Head
            ax.text(
                st["x"] + 4.8, item_y - 2.2,
                head,
                color=navy_dark, fontsize=8.8, fontweight="bold",
                ha="left", va="center", zorder=5, fontfamily="sans-serif"
            )
            # Item Desc
            ax.text(
                st["x"] + 4.8, item_y - 6.6,
                desc,
                color="#475569", fontsize=7.6, fontweight="normal",
                ha="left", va="center", zorder=5, fontfamily="sans-serif"
            )

    # Connecting Arrows between stages
    arrow_positions = [
        (23.9, 50),
        (48.7, 50),
        (73.5, 50)
    ]
    for ax_pos, ay_pos in arrow_positions:
        ax.text(
            ax_pos + 1.4, ay_pos, "➔",
            color="#2563eb", fontsize=22, fontweight="black",
            ha="center", va="center", zorder=10
        )

    plt.tight_layout()
    plt.savefig(output_path, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Generated clean architecture diagram at {output_path}")

if __name__ == "__main__":
    out = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\architecture_diagram.png"
    create_system_architecture_diagram(out)
