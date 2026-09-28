import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

out_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation"
os.makedirs(out_dir, exist_ok=True)

# 1. Generate Runway Skyline Banner for Slide 4 (Airport Runway & Modern Airliner at Night/Sunset or Crisp Daylight)
def make_runway_banner():
    fig, ax = plt.subplots(figsize=(13.333, 1.4), dpi=200)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 20)
    ax.axis('off')

    # Sky gradient / soft background
    # City / Airport Skyline silhouette
    buildings = [(2, 8, 4), (7, 12, 3.5), (11, 7, 5), (17, 10, 3), (21, 6, 6), 
                 (28, 9, 4), (33, 14, 5), (39, 8, 3.5), (75, 11, 4), (80, 15, 6),
                 (87, 9, 3), (91, 13, 5), (97, 8, 4)]
    for bx, by, bw in buildings:
        ax.add_patch(patches.Rectangle((bx, 3), bw, by, facecolor='#CBD5E1', edgecolor='none', alpha=0.6))
        # Add small windows
        for wx in np.linspace(bx+0.5, bx+bw-0.5, 3):
            for wy in np.linspace(4, 3+by-1, 4):
                ax.add_patch(patches.Rectangle((wx, wy), 0.3, 0.4, facecolor='#FFFFFF', alpha=0.8))

    # Control Tower silhouette
    ax.add_patch(patches.Rectangle((55, 3), 3, 11, facecolor='#94A3B8', edgecolor='none'))
    ax.add_patch(patches.Polygon([[53.5, 14], [59.5, 14], [58, 17], [55, 17]], facecolor='#64748B'))
    ax.add_patch(patches.Rectangle((56.3, 17), 0.4, 2.5, facecolor='#E2E8F0')) # Antenna

    # Airport Terminal Roof Arc
    t_x = np.linspace(42, 70, 100)
    t_y = 7 + 2.5 * np.sin((t_x - 42) / 28 * np.pi)
    ax.fill_between(t_x, 3, t_y, color='#94A3B8', alpha=0.5)

    # Ground / Tarmac
    ax.add_patch(patches.Rectangle((0, 0), 100, 3.5, facecolor='#1E293B'))
    # Runway center dashed markings
    for mx in range(2, 98, 8):
        ax.add_patch(patches.Rectangle((mx, 1.5), 4.5, 0.4, facecolor='#F8FAFC'))
    # Runway edge yellow lines
    ax.plot([0, 100], [3.2, 3.2], color='#FBBF24', lw=2)
    ax.plot([0, 100], [0.2, 0.2], color='#FBBF24', lw=2)
    
    # Runway threshold stripes on left
    for ty in np.linspace(0.5, 2.9, 7):
        ax.add_patch(patches.Rectangle((1, ty), 2.5, 0.2, facecolor='#FFFFFF'))

    # Taxiing aircraft silhouette on runway
    # Fuselage
    ax.add_patch(patches.Ellipse((72, 3.8), 16, 2.6, facecolor='#1E3A8A', edgecolor='#2563EB', lw=1.5))
    # Tail fin
    ax.add_patch(patches.Polygon([[78, 4.8], [80.5, 4.8], [82, 8.5], [79.5, 8.5]], facecolor='#DC2626', edgecolor='none'))
    # Wing
    ax.add_patch(patches.Polygon([[69, 3.8], [74, 3.8], [71, 1.8], [67, 1.8]], facecolor='#3B82F6'))
    # Engines
    ax.add_patch(patches.Ellipse((70, 2.4), 2.2, 0.8, facecolor='#475569'))
    # Nose cone
    ax.add_patch(patches.Polygon([[64, 3.8], [64.5, 4.4], [64.5, 3.2]], facecolor='#1E3A8A'))
    
    # Jet engine contrail / flight path line
    ax.plot([15, 60], [13, 8], color='#38BDF8', lw=2, ls='--', alpha=0.8)
    # Airborne small plane icon taking off
    ax.scatter([15], [13], marker='>', s=140, color='#0284C7', zorder=10)

    # Runway green threshold lights
    for lx in np.linspace(4, 96, 24):
        ax.scatter([lx], [3.2], color='#22C55E', s=16, zorder=5)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    p_path = os.path.join(out_dir, "runway_skyline_banner.png")
    fig.savefig(p_path, dpi=200, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    print(f"Generated {p_path}")

# 2. Flight Surge Callout Card for Slide 2 (Circle / Badge showing dynamic pricing surge)
def make_surge_callout():
    fig, ax = plt.subplots(figsize=(4.5, 4.5), dpi=200)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Circular Badge with vibrant shadow border
    outer_circle = patches.Circle((5, 5), 4.7, facecolor='#0F172A', edgecolor='#38BDF8', lw=3)
    ax.add_patch(outer_circle)
    inner_circle = patches.Circle((5, 5), 4.3, facecolor='#1E293B', edgecolor='#64748B', lw=1.2)
    ax.add_patch(inner_circle)

    # Header text
    ax.text(5, 8.2, "AIRFARE DYNAMIC SURGE", color='#F8FAFC', fontsize=11, fontweight='bold', ha='center')
    ax.text(5, 7.5, "DEL → BOM (IndiGo 6E-2041)", color='#94A3B8', fontsize=8.5, ha='center')

    # Surge badge pill
    ax.add_patch(patches.FancyBboxPatch((2.2, 5.8), 5.6, 1.3, boxstyle="round,pad=0.2", facecolor='#EF4444', edgecolor='none'))
    ax.text(5, 6.35, "₹7,644", color='#FFFFFF', fontsize=19, fontweight='heavy', ha='center', va='center')
    ax.text(5, 5.5, "T+1 Emergency Booking (+86% Surge)", color='#FCA5A5', fontsize=8, fontweight='bold', ha='center')

    # Normal saver price below
    ax.add_patch(patches.FancyBboxPatch((2.2, 3.7), 5.6, 1.1, boxstyle="round,pad=0.2", facecolor='#065F46', edgecolor='none'))
    ax.text(5, 4.2, "₹4,106", color='#FFFFFF', fontsize=15, fontweight='bold', ha='center', va='center')
    ax.text(5, 3.4, "T+45 Saver Advance Rate", color='#6EE7B7', fontsize=8, ha='center')

    # Warning alert footer
    ax.text(5, 2.2, "⚠️ 1 Monthly Manual Visit Misses", color='#FBBF24', fontsize=9, fontweight='bold', ha='center')
    ax.text(5, 1.5, "Entire 200–400% Intraday Yield Volatility", color='#E2E8F0', fontsize=7.5, ha='center')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    p_path = os.path.join(out_dir, "flight_surge_callout.png")
    fig.savefig(p_path, dpi=200, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f"Generated {p_path}")

# 3. Manual to Digital Visual Callout for Slide 5 ("From Stale Manual Quotes -> Real-Time Sovereign Intelligence")
def make_manual_to_digital():
    fig, ax = plt.subplots(figsize=(6.5, 2.4), dpi=200)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis('off')

    # Container outline
    card_bg = patches.FancyBboxPatch((1, 1), 98, 38, boxstyle="round,pad=1.5", facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=1.5)
    ax.add_patch(card_bg)

    # Title Bar
    ax.text(50, 34, "From Stale Manual Field Quotes  ➔  To Real-Time Sovereign Intelligence", 
            color='#1E293B', fontsize=10.5, fontweight='bold', ha='center')

    # Left Box: Traditional Manual MoSPI
    left_box = patches.FancyBboxPatch((4, 4), 40, 26, boxstyle="round,pad=1", facecolor='#FEF2F2', edgecolor='#EF4444', lw=1.5)
    ax.add_patch(left_box)
    ax.text(24, 25, "PAST: MANUAL AUDIT", color='#991B1B', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(24, 19, "• 1 Single Quote / Month", color='#7F1D1D', fontsize=8.5, ha='center')
    ax.text(24, 14, "• 15-Day Survey Lag", color='#7F1D1D', fontsize=8.5, ha='center')
    ax.text(24, 9, "• ₹15+ Cr / Yr Field Cost", color='#7F1D1D', fontsize=8.5, ha='center')

    # Center Transition Arrow
    ax.annotate("", xy=(53, 17), xytext=(47, 17),
                arrowprops=dict(arrowstyle="->", lw=3, color='#2563EB'))

    # Right Box: VayuSuchak APIx
    right_box = patches.FancyBboxPatch((56, 4), 40, 26, boxstyle="round,pad=1", facecolor='#F0FDF4', edgecolor='#16A34A', lw=1.5)
    ax.add_patch(right_box)
    ax.text(76, 25, "FUTURE: VAYUSUCHAK APIx", color='#166534', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(76, 19, "• 10,000+ Daily Quotes", color='#14532D', fontsize=8.5, ha='center')
    ax.text(76, 14, "• Real-Time (0-Day Lag)", color='#14532D', fontsize=8.5, ha='center')
    ax.text(76, 9, "• < ₹3,500 / Mo Serverless", color='#14532D', fontsize=8.5, ha='center')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    p_path = os.path.join(out_dir, "manual_to_digital_callout.png")
    fig.savefig(p_path, dpi=200, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f"Generated {p_path}")

if __name__ == "__main__":
    make_runway_banner()
    make_surge_callout()
    make_manual_to_digital()
