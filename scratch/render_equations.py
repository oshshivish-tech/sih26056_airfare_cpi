import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 18,
    'mathtext.fontset': 'cm',
    'text.usetex': False
})

# Equation 1: Jevons Geometric Mean (Elementary Index)
fig, ax = plt.subplots(figsize=(8.0, 1.25))
ax.axis('off')
eq1 = r'$I_{\mathrm{Jevons}}^t = \left( \prod_{i=1}^N \frac{P_{i,t}}{P_{i,0}} \right)^{\frac{1}{N}} \times 100 = \exp\left( \frac{1}{N} \sum_{i=1}^N \ln\left( \frac{P_{i,t}}{P_{i,0}} \right) \right) \times 100$'
ax.text(0.5, 0.5, eq1, fontsize=18, ha='center', va='center', color='#050811')
plt.savefig('scratch/eq_jevons_hd.png', dpi=500, transparent=True, bbox_inches='tight', pad_inches=0.015)
plt.close()

# Equation 2: DGCA Volume Weighted Composite Index
fig, ax = plt.subplots(figsize=(6.8, 1.05))
ax.axis('off')
eq2 = r'$I_{\mathrm{Composite}}^t = \sum_{c=1}^C w_c \cdot I_{c,t} \quad \left(\mathrm{where}\ \sum_{c=1}^C w_c = 1.0\right)$'
ax.text(0.5, 0.5, eq2, fontsize=18, ha='center', va='center', color='#050811')
plt.savefig('scratch/eq_composite_hd.png', dpi=500, transparent=True, bbox_inches='tight', pad_inches=0.015)
plt.close()

print('Rendered ultra-large 500 DPI HD equations!')
