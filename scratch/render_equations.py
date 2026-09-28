import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 15,
    'mathtext.fontset': 'cm',
    'text.usetex': False
})

# Equation 1: Jevons
fig, ax = plt.subplots(figsize=(7.5, 1.1))
ax.axis('off')
eq1 = r'$I_{\mathrm{Jevons}}^t = \left( \prod_{i=1}^N \frac{P_{i,t}}{P_{i,0}} \right)^{\frac{1}{N}} \times 100 = \exp\left( \frac{1}{N} \sum_{i=1}^N \ln\left( \frac{P_{i,t}}{P_{i,0}} \right) \right) \times 100$'
ax.text(0.5, 0.5, eq1, fontsize=15.5, ha='center', va='center', color='#090d16', weight='bold')
plt.savefig('scratch/eq_jevons_hd.png', dpi=450, transparent=True, bbox_inches='tight', pad_inches=0.02)
plt.close()

# Equation 2: Composite
fig, ax = plt.subplots(figsize=(6.2, 0.95))
ax.axis('off')
eq2 = r'$I_{\mathrm{Composite}}^t = \sum_{c=1}^C w_c \cdot I_{c,t} \quad \left(\mathrm{where}\ \sum_{c=1}^C w_c = 1.0\right)$'
ax.text(0.5, 0.5, eq2, fontsize=15.5, ha='center', va='center', color='#090d16', weight='bold')
plt.savefig('scratch/eq_composite_hd.png', dpi=450, transparent=True, bbox_inches='tight', pad_inches=0.02)
plt.close()

print('HD equations re-rendered with larger font & 450 DPI!')
