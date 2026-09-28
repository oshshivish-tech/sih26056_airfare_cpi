import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_perfect_workflow_strip(output_path):
    # Width 16, Height 2.65 -> aspect ratio ~6.03:1
    fig, ax = plt.subplots(figsize=(16, 2.65), dpi=300)
    ax.set_aspect('equal')
    ax.set_facecolor('none')
    fig.patch.set_facecolor('none')

    # 5 Centers spanning horizontally
    cx = [1.5, 4.4, 7.3, 10.2, 13.1]
    cy = 1.48
    r_outer = 0.78
    r_inner = 0.65

    colors = [
        {"ring": "#1d4ed8", "bg": "#eff6ff", "icon": "#1e3a8a", "title": "1. Dynamic\nYield Tracking", "sub": "T+1..T+45"},
        {"ring": "#0284c7", "bg": "#f0f9ff", "icon": "#0369a1", "title": "2. Dynamic\nIQR Scrubber", "sub": "Base fare isolation"},
        {"ring": "#0d9488", "bg": "#f0fdfa", "icon": "#0f766e", "title": "3. UN/ILO\nJevons Index", "sub": "Eliminates bias"},
        {"ring": "#16a34a", "bg": "#f0fdf4", "icon": "#15803d", "title": "4. Sovereign\nAudit Vault", "sub": "SHA-256 Provenance"},
        {"ring": "#059669", "bg": "#ecfdf5", "icon": "#047857", "title": "5. Real-Time\nAPI Delivery", "sub": "Sub-10ms feed"}
    ]

    for i in range(5):
        c = colors[i]
        x = cx[i]

        # Outer ring (thick border, crisp white background)
        outer_circle = patches.Circle((x, cy), r_outer, edgecolor=c["ring"], facecolor='#ffffff', linewidth=3.8, zorder=3)
        ax.add_patch(outer_circle)

        # Inner tinted circle
        inner_circle = patches.Circle((x, cy), r_inner, edgecolor=c["ring"], facecolor=c["bg"], linewidth=1.6, zorder=4)
        ax.add_patch(inner_circle)

        # Draw connecting arrows between circles
        if i < 4:
            x_start = x + r_outer + 0.12
            x_end = cx[i+1] - r_outer - 0.12
            ax.annotate('', xy=(x_end, cy), xytext=(x_start, cy),
                        arrowprops=dict(arrowstyle="->,head_length=0.42,head_width=0.25",
                                        color="#64748b", lw=2.4), zorder=2)

        # Text below: Title
        ax.text(x, cy - r_outer - 0.18, c["title"], ha='center', va='top',
                fontsize=11.2, fontweight='bold', color='#0f172a', linespacing=1.08, family='sans-serif')
        # Text below: Subtitle (snug under title)
        ax.text(x, cy - r_outer - 0.58, c["sub"], ha='center', va='top',
                fontsize=9.6, fontweight='normal', color='#475569', family='sans-serif')

    # Draw Icons inside each circle
    # 1. Yield Tracking Icon: Speedometer / Radar wave + dynamic booking curve
    x1 = cx[0]
    theta = np.linspace(np.pi*0.2, np.pi*0.8, 30)
    ax.plot(x1 + 0.32*np.cos(theta), cy - 0.08 + 0.40*np.sin(theta), color=colors[0]["icon"], lw=2.8, zorder=5)
    ax.plot(x1 + 0.20*np.cos(theta), cy - 0.08 + 0.26*np.sin(theta), color=colors[0]["icon"], lw=2.2, zorder=5)
    ax.scatter([x1], [cy - 0.08], color=colors[0]["icon"], s=40, zorder=5)
    ax.annotate('', xy=(x1 + 0.28, cy + 0.25), xytext=(x1 - 0.25, cy - 0.22),
                arrowprops=dict(arrowstyle="->,head_length=0.32,head_width=0.20", color=colors[0]["icon"], lw=2.5), zorder=5)

    # 2. Funnel (IQR Scrubber)
    x2 = cx[1]
    funnel_pts = np.array([
        [x2 - 0.32, cy + 0.28],
        [x2 + 0.32, cy + 0.28],
        [x2 + 0.10, cy - 0.04],
        [x2 + 0.10, cy - 0.32],
        [x2 - 0.10, cy - 0.32],
        [x2 - 0.10, cy - 0.04]
    ])
    funnel = patches.Polygon(funnel_pts, closed=True, edgecolor=colors[1]["icon"], facecolor='#e0f2fe', linewidth=2.5, zorder=5)
    ax.add_patch(funnel)
    ax.plot([x2 - 0.24, x2 + 0.24], [cy + 0.16, cy + 0.16], color=colors[1]["icon"], lw=1.8, zorder=5)
    ax.plot([x2 - 0.16, x2 + 0.16], [cy + 0.05, cy + 0.05], color=colors[1]["icon"], lw=1.8, zorder=5)

    # 3. Sigma (UN/ILO Jevons Index)
    x3 = cx[2]
    ax.text(x3, cy - 0.02, r'$\sum$', ha='center', va='center', fontsize=35, fontweight='bold',
            color=colors[2]["icon"], zorder=5, family='serif')

    # 4. Shield (Sovereign Audit Vault)
    x4 = cx[3]
    shield_pts = np.array([
        [x4 - 0.30, cy + 0.28],
        [x4 + 0.30, cy + 0.28],
        [x4 + 0.30, cy - 0.03],
        [x4, cy - 0.34],
        [x4 - 0.30, cy - 0.03]
    ])
    shield = patches.Polygon(shield_pts, closed=True, edgecolor=colors[3]["icon"], facecolor='#dcfce7', linewidth=2.5, zorder=5)
    ax.add_patch(shield)
    ax.plot([x4 - 0.16, x4 - 0.03, x4 + 0.18], [cy + 0.02, cy - 0.12, cy + 0.14],
            color=colors[3]["icon"], lw=3.2, solid_capstyle='round', zorder=6)

    # 5. API / Terminal Badge (Real-Time API Delivery)
    x5 = cx[4]
    api_box = patches.FancyBboxPatch((x5 - 0.32, cy - 0.20), 0.64, 0.40,
                                     boxstyle="round,pad=0.03,rounding_size=0.08",
                                     edgecolor=colors[4]["icon"], facecolor='#d1fae5', linewidth=2.5, zorder=5)
    ax.add_patch(api_box)
    ax.text(x5, cy - 0.01, "API", ha='center', va='center', fontsize=15, fontweight='bold',
            color=colors[4]["icon"], zorder=6, family='sans-serif')
    ax.scatter([x5 - 0.16, x5, x5 + 0.16], [cy + 0.30, cy + 0.30, cy + 0.30],
               color=colors[4]["icon"], s=24, zorder=5)

    ax.set_xlim(0.0, 14.6)
    ax.set_ylim(0.0, 2.45)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
    plt.close()
    print("Created perfect workflow strip at", output_path)

if __name__ == "__main__":
    out = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation\workflow_circular_nodes.png"
    create_perfect_workflow_strip(out)
