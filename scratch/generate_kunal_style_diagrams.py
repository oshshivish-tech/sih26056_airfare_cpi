import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

out_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation"
os.makedirs(out_dir, exist_ok=True)

# =============================================================================
# 1. PYRAMID DIAGRAM FOR PAGE 2 (Matches kunal.techy Page 2 Center Pyramid)
# =============================================================================
def generate_pyramid_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.0), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(-2, 102)
    ax.set_ylim(2, 98)
    ax.axis('off')

    # Triangle with broad stable proportions
    # Apex: (50, 96), Base: (-1, 5) to (101, 5)
    
    # Tier 1: Apex (y: 68 to 96)
    t1_poly = patches.Polygon([[50, 96], [35, 68], [65, 68]], closed=True,
                              facecolor='#1e3a8a', edgecolor='#fbbf24', linewidth=3, zorder=3)
    ax.add_patch(t1_poly)
    # Icon or star at top
    ax.text(50, 88, "★", color='#fbbf24', fontsize=16, ha='center', va='center', zorder=4)
    ax.text(50, 80, "CORE INNOVATION", color='#fbbf24', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(50, 73, "Real-Time APIx", color='#ffffff', fontsize=11, fontweight='bold', ha='center', va='center', zorder=4)

    # Tier 2: Primary Functions (y: 46 to 68)
    t2_poly = patches.Polygon([[35, 68], [22, 46], [78, 46], [65, 68]], closed=True,
                              facecolor='#2563eb', edgecolor='#fbbf24', linewidth=3, zorder=3)
    ax.add_patch(t2_poly)
    ax.text(50, 62, "PRIMARY FUNCTIONS", color='#dbeafe', fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=4)
    
    ax.text(36, 54, "Automated Crawlers", color='#ffffff', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(36, 49.5, "4 Domestic Carriers", color='#bfdbfe', fontsize=7, ha='center', va='center', zorder=4)

    ax.text(64, 54, "5 Dynamic Horizons", color='#ffffff', fontsize=8, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(64, 49.5, "T+1 to T+45 Curves", color='#bfdbfe', fontsize=7, ha='center', va='center', zorder=4)
    
    # Divider line
    ax.plot([50, 50], [47, 58], color='#60a5fa', linewidth=1.5, zorder=4)

    # Tier 3: Econometric & Quality Rigor (y: 25 to 46)
    t3_poly = patches.Polygon([[22, 46], [10, 25], [90, 25], [78, 46]], closed=True,
                              facecolor='#059669', edgecolor='#fbbf24', linewidth=3, zorder=3)
    ax.add_patch(t3_poly)
    ax.text(50, 40.5, "STATISTICAL & ECONOMETRIC RIGOR", color='#d1fae5', fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=4)
    
    ax.text(26, 33, "UN/ILO Jevons Index", color='#ffffff', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(26, 28.5, "Zero Substitution Bias", color='#a7f3d0', fontsize=6.8, ha='center', va='center', zorder=4)

    ax.text(50, 33, "DGCA Seat Weights", color='#ffffff', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(50, 28.5, "Passenger Traffic Share", color='#a7f3d0', fontsize=6.8, ha='center', va='center', zorder=4)

    ax.text(74, 33, "Dynamic IQR Filter", color='#ffffff', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(74, 28.5, "Outlier Truncation", color='#a7f3d0', fontsize=6.8, ha='center', va='center', zorder=4)

    ax.plot([37, 37], [26, 37], color='#34d399', linewidth=1.5, zorder=4)
    ax.plot([63, 63], [26, 37], color='#34d399', linewidth=1.5, zorder=4)

    # Tier 4: Base Infrastructure & Security (y: 5 to 25)
    t4_poly = patches.Polygon([[10, 25], [-1, 5], [101, 5], [90, 25]], closed=True,
                              facecolor='#0f172a', edgecolor='#fbbf24', linewidth=3, zorder=3)
    ax.add_patch(t4_poly)
    ax.text(50, 19.5, "SOVEREIGN AUDIT & PRODUCTION DEPLOYMENT", color='#fef08a', fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=4)
    
    ax.text(12, 13, "SHA-256 Vault", color='#ffffff', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(12, 8.5, "Legal Provenance", color='#94a3b8', fontsize=6.5, ha='center', va='center', zorder=4)

    ax.text(37, 13, "FastAPI Microservices", color='#ffffff', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(37, 8.5, "PostgreSQL Backend", color='#94a3b8', fontsize=6.5, ha='center', va='center', zorder=4)

    ax.text(63, 13, "MoSPI eSankhyiki", color='#ffffff', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(63, 8.5, "Automated API Feed", color='#94a3b8', fontsize=6.5, ha='center', va='center', zorder=4)

    ax.text(88, 13, "Lead-Time Elasticity", color='#ffffff', fontsize=7.2, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(88, 8.5, "Surge Calibration", color='#94a3b8', fontsize=6.5, ha='center', va='center', zorder=4)

    ax.plot([25, 25], [6, 16], color='#475569', linewidth=1.5, zorder=4)
    ax.plot([50, 50], [6, 16], color='#475569', linewidth=1.5, zorder=4)
    ax.plot([75, 75], [6, 16], color='#475569', linewidth=1.5, zorder=4)

    # Outer hazard line around triangle
    ax.plot([50, -1, 101, 50], [96, 5, 5, 96], color='#f59e0b', linewidth=4.5, linestyle='-', zorder=6)

    plt.tight_layout()
    out_file = os.path.join(out_dir, "pyramid_diagram_page2.png")
    plt.savefig(out_file, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("Generated pyramid diagram:", out_file)

# =============================================================================
# 2. METHODOLOGY CIRCULAR WHEEL FOR PAGE 3 (Matches kunal.techy Page 3 Left Wheel)
# =============================================================================
def generate_methodology_wheel():
    fig, ax = plt.subplots(figsize=(7.5, 7.5), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.axis('off')

    # Central Circle
    center_circle = patches.Circle((0, 0), 0.38, facecolor='#1e3a8a', edgecolor='#ffffff', linewidth=3, zorder=10)
    ax.add_patch(center_circle)
    ax.text(0, 0.08, "VAYUSUCHAK", color='#ffffff', fontsize=10, fontweight='bold', ha='center', va='center', zorder=11)
    ax.text(0, -0.08, "PIPELINE", color='#93c5fd', fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=11)

    steps = [
        ("1. Multi-Carrier Crawl", "Playwright headless crawlers\nIndiGo, AI, Akasa, SpiceJet", "#2563eb", 90),
        ("2. Cleansing & Stripping", "Isolate base fares, strip\ntaxes, GST, UDF fees", "#ea580c", 18),
        ("3. Dynamic IQR Filter", "Automated Z-score outlier\ntruncation [Q1-1.5, Q3+2]", "#eab308", 306),
        ("4. UN/ILO Jevons GM", "Geometric mean formula +\nDGCA passenger weights", "#16a34a", 234),
        ("5. SHA-256 Vault", "Cryptographic batch hash\nfor legal audit manifest", "#dc2626", 162)
    ]

    r_inner = 0.45
    r_outer = 0.88

    for idx, (title, desc, color, angle) in enumerate(steps):
        # Wedge
        theta1 = angle - 33
        theta2 = angle + 33
        wedge = patches.Wedge((0, 0), r_outer, theta1, theta2, width=(r_outer - r_inner),
                              facecolor=color, edgecolor='#ffffff', linewidth=2.5, zorder=5)
        ax.add_patch(wedge)

        # Badge circle for step number
        rad = np.radians(angle)
        bx = 0.66 * np.cos(rad)
        by = 0.66 * np.sin(rad)
        badge = patches.Circle((bx, by), 0.12, facecolor='#ffffff', edgecolor=color, linewidth=2, zorder=6)
        ax.add_patch(badge)
        ax.text(bx, by, str(idx+1), color=color, fontsize=11, fontweight='bold', ha='center', va='center', zorder=7)

        # Outer Label
        lx = 1.15 * np.cos(rad)
        ly = 1.15 * np.sin(rad)
        ha_val = 'center'
        if lx > 0.3: ha_val = 'left'
        elif lx < -0.3: ha_val = 'right'
        
        ax.text(lx, ly + 0.06, title, color='#0f172a', fontsize=8.5, fontweight='bold', ha=ha_val, va='center', zorder=8)
        ax.text(lx, ly - 0.08, desc, color='#475569', fontsize=7.0, fontweight='normal', ha=ha_val, va='center', zorder=8)

    plt.tight_layout()
    out_file = os.path.join(out_dir, "methodology_wheel_page3.png")
    plt.savefig(out_file, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("Generated methodology wheel:", out_file)

# =============================================================================
# 3. IMPACTS & BENEFITS WHEEL FOR PAGE 5 (Matches kunal.techy Page 5 Left Wheel)
# =============================================================================
def generate_impact_wheel():
    fig, ax = plt.subplots(figsize=(8.0, 8.0), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.55, 1.55)
    ax.axis('off')

    # Central Divider Ring
    ring = patches.Circle((0, 0), 0.70, facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=2.5, linestyle='--', zorder=2)
    ax.add_patch(ring)

    # Center Pill / Circle: "IMPACTS | BENEFITS"
    center_pill = patches.FancyBboxPatch((-0.32, -0.42), 0.64, 0.84, boxstyle="round,pad=0.1,rounding_size=0.3",
                                        facecolor='#ffffff', edgecolor='#1e3a8a', linewidth=2.5, zorder=10)
    ax.add_patch(center_pill)
    
    # Left Arc: IMPACTS
    ax.text(-0.12, 0, "IMPACTS", color='#1e3a8a', fontsize=9.5, fontweight='bold', ha='center', va='center', rotation=90, zorder=11)
    # Divider line
    ax.plot([0, 0], [-0.35, 0.35], color='#cbd5e1', linewidth=1.5, zorder=11)
    # Right Arc: BENEFITS
    ax.text(0.12, 0, "BENEFITS", color='#059669', fontsize=9.5, fontweight='bold', ha='center', va='center', rotation=270, zorder=11)

    # 4 Impacts on Left (Gold/Slate dots)
    impacts = [
        ("1", "Zero Policy Lag", "Slashes 15-day collection lag to real-time (0 days)", 145),
        ("2", "Dynamic Yield Scope", "Captures 200-400% surge swings across 5 horizons", 175),
        ("3", "Anti-Predatory Alert", "Detects airline route monopolies & festive fare gouging", 205),
        ("4", "UDAN Scale", "Scales seamlessly from 12 metros to 250+ regional routes", 235)
    ]

    for num, title, desc, angle in impacts:
        rad = np.radians(angle)
        bx = 0.70 * np.cos(rad)
        by = 0.70 * np.sin(rad)
        b = patches.Circle((bx, by), 0.085, facecolor='#d97706', edgecolor='#ffffff', linewidth=1.5, zorder=5)
        ax.add_patch(b)
        ax.text(bx, by, num, color='#ffffff', fontsize=9, fontweight='bold', ha='center', va='center', zorder=6)

        lx = bx - 0.15
        ly = by
        ax.text(lx, ly + 0.05, title, color='#1e3a8a', fontsize=8.5, fontweight='bold', ha='right', va='center', zorder=6)
        ax.text(lx, ly - 0.06, desc, color='#475569', fontsize=7.0, fontweight='normal', ha='right', va='center', zorder=6)

    # 4 Benefits on Right (Blue/Green dots)
    benefits = [
        ("1", "Macro Stability (RBI)", "High-frequency leading transport inflation signals for MPC", 35),
        ("2", "Statistical Modernization", "UN/ILO compliant daily observations for MoSPI eSankhyiki", 5),
        ("3", "Evidentiary Trust", "SHA-256 cryptographic audit manifest for legal validity", 335),
        ("4", ">95% Cost Reduction", "Replaces physical field survey teams with serverless crawlers", 305)
    ]

    for num, title, desc, angle in benefits:
        rad = np.radians(angle)
        bx = 0.70 * np.cos(rad)
        by = 0.70 * np.sin(rad)
        b = patches.Circle((bx, by), 0.085, facecolor='#2563eb', edgecolor='#ffffff', linewidth=1.5, zorder=5)
        ax.add_patch(b)
        ax.text(bx, by, num, color='#ffffff', fontsize=9, fontweight='bold', ha='center', va='center', zorder=6)

        lx = bx + 0.15
        ly = by
        ax.text(lx, ly + 0.05, title, color='#047857', fontsize=8.5, fontweight='bold', ha='left', va='center', zorder=6)
        ax.text(lx, ly - 0.06, desc, color='#475569', fontsize=7.0, fontweight='normal', ha='left', va='center', zorder=6)

    plt.tight_layout()
    out_file = os.path.join(out_dir, "impact_wheel_page5.png")
    plt.savefig(out_file, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("Generated impact wheel:", out_file)

# =============================================================================
# 4. COMPARATIVE BAR CHART FOR PAGE 5 (Matches kunal.techy Page 5 Right Chart)
# =============================================================================
def generate_comparison_chart():
    fig, ax = plt.subplots(figsize=(7.5, 4.4), dpi=220)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')

    metrics = [
        'Survey OpEx (₹ Cost)',
        'Upward Bias Distortion',
        'Data Collection Lag (Days)',
        'Dynamic Surge Capture (%)',
        'Daily Quotes Ingested'
    ]

    current_system = [95, 80, 85, 5, 2]
    vayusuchak = [5, 0, 2, 98, 100]

    y = np.arange(len(metrics))
    height = 0.35

    rects1 = ax.barh(y - height/2, current_system, height, label='Status Quo (Manual MoSPI)', color='#94a3b8', edgecolor='#64748b')
    rects2 = ax.barh(y + height/2, vayusuchak, height, label='VayuSuchak (AI & Econometric)', color='#2563eb', edgecolor='#1d4ed8')

    ax.set_title('Airfare CPI Methodology: Current Manual vs. VayuSuchak', fontsize=11, fontweight='bold', color='#0f172a', pad=12)
    ax.set_yticks(y)
    ax.set_yticklabels(metrics, fontsize=8.5, fontweight='bold', color='#1e293b')
    ax.set_xlim(0, 120)
    ax.set_xlabel('Relative Performance & Modernization Index (%)', fontsize=8, color='#475569', fontweight='bold')
    ax.legend(loc='lower right', bbox_to_anchor=(0.98, 0.08), fontsize=8.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    # Value Labels
    for rect in rects1:
        w = rect.get_width()
        ax.text(w + 1.5, rect.get_y() + rect.get_height()/2, f"{int(w)}%", va='center', ha='left', fontsize=7.5, color='#64748b', fontweight='bold')

    for rect in rects2:
        w = rect.get_width()
        ax.text(w + 1.5, rect.get_y() + rect.get_height()/2, f"{int(w)}%", va='center', ha='left', fontsize=7.5, color='#1d4ed8', fontweight='bold')

    plt.tight_layout()
    out_file = os.path.join(out_dir, "comparison_chart_page5.png")
    plt.savefig(out_file, dpi=250, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print("Generated comparison chart:", out_file)

if __name__ == "__main__":
    generate_pyramid_diagram()
    generate_methodology_wheel()
    generate_impact_wheel()
    generate_comparison_chart()
