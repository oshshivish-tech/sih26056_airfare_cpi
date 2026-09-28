import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_problem_solution_diagram(output_path):
    # Dimensions: 13.5 x 7.2 inches at 220 dpi
    fig, ax = plt.subplots(figsize=(13.5, 7.0), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    navy_dark = '#0f172a'
    slate_border = '#cbd5e1'

    # =========================================================================
    # ROW 1: THE CRITICAL PROBLEM (LEGACY MANUAL SURVEY)
    # =========================================================================
    p_bg = patches.FancyBboxPatch(
        (2, 53), 96, 44,
        boxstyle="round,pad=0.5,rounding_size=1.5",
        edgecolor="#fca5a5", facecolor="#fff5f5", linewidth=1.5, zorder=2
    )
    ax.add_patch(p_bg)

    # Problem Header Badge
    ax.text(
        4.5, 93.5,
        "✖ CRITICAL DEFICIENCY IN STATUS QUO MANUAL PRICE COLLECTION",
        color="#991b1b", fontsize=11.5, fontweight="bold", ha="left", va="center", fontfamily="sans-serif", zorder=3
    )
    ax.text(
        4.5, 88.5,
        "MoSPI field surveyors manually record static airfares from limited offline outlets, creating systemic policy vulnerabilities:",
        color="#7f1d1d", fontsize=8.6, fontweight="normal", ha="left", va="center", fontfamily="sans-serif", zorder=3
    )

    # 4 Problem Flow Steps
    prob_steps = [
        ("1. PHYSICAL OUTLETS", "Surveyor travels to city ticketing agent", "Limited Coverage (<0.1% routes)", "#ef4444"),
        ("2. STATIC SPOT QUOTE", "Records single counter price on clipboard", "Blind to 90%+ Online Sales", "#dc2626"),
        ("3. 15-DAY POLICY LAG", "Manual entry into central CPI database", "Stale by publication date", "#b91c1c"),
        ("4. DISTORTED CPI", "Arithmetic mean causes upward bias", "Misses 200-400% surge swings", "#991b1b")
    ]

    for idx, (title, sub, badge, col) in enumerate(prob_steps):
        sx = 4.5 + (idx * 23.5)
        sy = 57.5
        sw = 21.0
        sh = 27.5

        # Step card
        c = patches.FancyBboxPatch(
            (sx, sy), sw, sh,
            boxstyle="round,pad=0.3,rounding_size=1.0",
            edgecolor="#fecaca", facecolor="#ffffff", linewidth=1.2, zorder=3
        )
        ax.add_patch(c)

        # Title
        ax.text(sx + sw/2, sy + sh - 4.8, title, color=col, fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=4)
        # Subtitle
        ax.text(sx + sw/2, sy + sh - 11.5, sub, color="#475569", fontsize=7.6, fontweight="normal", ha="center", va="center", zorder=4)
        
        # Badge
        b = patches.FancyBboxPatch(
            (sx + 1.5, sy + 3.2), sw - 3.0, 5.5,
            boxstyle="round,pad=0.2,rounding_size=0.8",
            edgecolor=col, facecolor="#fee2e2", linewidth=0.8, zorder=4
        )
        ax.add_patch(b)
        ax.text(sx + sw/2, sy + 5.9, badge, color=col, fontsize=7.4, fontweight="bold", ha="center", va="center", zorder=5)

        # Arrow to next step
        if idx < 3:
            ax.text(sx + sw + 1.25, sy + sh/2, "➔", color="#ef4444", fontsize=16, fontweight="black", ha="center", va="center", zorder=6)

    # =========================================================================
    # ROW 2: OUR SOVEREIGN SOLUTION (VAYUSUCHAK AUTOMATED PIPELINE)
    # =========================================================================
    s_bg = patches.FancyBboxPatch(
        (2, 4), 96, 45,
        boxstyle="round,pad=0.5,rounding_size=1.5",
        edgecolor="#86efac", facecolor="#f0fdf4", linewidth=1.5, zorder=2
    )
    ax.add_patch(s_bg)

    # Solution Header Badge
    ax.text(
        4.5, 45.0,
        "✔ VAYUSUCHAK (APIx): REAL-TIME SOVEREIGN AUTOMATED SOLUTION",
        color="#166534", fontsize=11.5, fontweight="bold", ha="left", va="center", fontfamily="sans-serif", zorder=3
    )
    ax.text(
        4.5, 40.0,
        "High-frequency autonomous web harvesters feed UN/ILO compliant econometric engines with cryptographic auditability:",
        color="#14532d", fontsize=8.6, fontweight="normal", ha="left", va="center", fontfamily="sans-serif", zorder=3
    )

    # 4 Solution Flow Steps
    sol_steps = [
        ("1. MULTI-CARRIER CRAWLER", "Playwright scrapers across IndiGo, AI, Akasa", "10,000+ Daily Quotes", "#16a34a"),
        ("2. 5 FORWARD HORIZONS", "Captures yield curves: T+1, T+7, T+15, T+30, T+45", "Full Dynamic Yield Curve", "#15803d"),
        ("3. UN/ILO JEVONS ENGINE", "Geometric mean + DGCA passenger weights", "Zero Substitution Bias", "#047857"),
        ("4. INSTANT DPI FEED", "SHA-256 Provenance Vault + FastAPI", "0-Day Real-Time CPI Sync", "#166534")
    ]

    for idx, (title, sub, badge, col) in enumerate(sol_steps):
        sx = 4.5 + (idx * 23.5)
        sy = 8.5
        sw = 21.0
        sh = 27.5

        # Step card
        c = patches.FancyBboxPatch(
            (sx, sy), sw, sh,
            boxstyle="round,pad=0.3,rounding_size=1.0",
            edgecolor="#bbf7d0", facecolor="#ffffff", linewidth=1.2, zorder=3
        )
        ax.add_patch(c)

        # Title
        ax.text(sx + sw/2, sy + sh - 4.8, title, color=col, fontsize=8.8, fontweight="bold", ha="center", va="center", zorder=4)
        # Subtitle
        ax.text(sx + sw/2, sy + sh - 11.5, sub, color="#475569", fontsize=7.6, fontweight="normal", ha="center", va="center", zorder=4)
        
        # Badge
        b = patches.FancyBboxPatch(
            (sx + 1.5, sy + 3.2), sw - 3.0, 5.5,
            boxstyle="round,pad=0.2,rounding_size=0.8",
            edgecolor=col, facecolor="#dcfce7", linewidth=0.8, zorder=4
        )
        ax.add_patch(b)
        ax.text(sx + sw/2, sy + 5.9, badge, color=col, fontsize=7.4, fontweight="bold", ha="center", va="center", zorder=5)

        # Arrow to next step
        if idx < 3:
            ax.text(sx + sw + 1.25, sy + sh/2, "➔", color="#16a34a", fontsize=16, fontweight="black", ha="center", va="center", zorder=6)

    plt.tight_layout()
    plt.savefig(output_path, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Generated clean Problem vs Solution diagram at {output_path}")

if __name__ == "__main__":
    out = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\problem_solution_diagram.png"
    create_problem_solution_diagram(out)
