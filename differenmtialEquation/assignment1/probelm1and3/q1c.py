from differenmtialEquation.assignment1.probelm1and3.helpers import *

def f(y, r): return y*(4-y) - r

fig = plt.figure(figsize=(16.5, 7.6))
gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1.3],
                       hspace=0.75, wspace=0.32)

ax_p1 = fig.add_subplot(gs[0, 0])
ax_p2 = fig.add_subplot(gs[1, 0])
ax_p3 = fig.add_subplot(gs[2, 0])
phase_line_panel(ax_p1, lambda y: f(y, 0), [0, 4], (-3, 7), label=r'$r=0<4$ (two equilibria)')
phase_line_panel(ax_p2, lambda y: f(y, 4), [2],    (-3, 7), label=r'$r=4$ (bifurcation pt.)')
phase_line_panel(ax_p3, lambda y: f(y, 6), [],     (-3, 7), label=r'$r=6>4$ (no equilibria)')

ax_f = fig.add_subplot(gs[:, 1])
ys = np.linspace(-3, 7, 400)
for rv, clr in [(0, '#1565c0'), (4, '#2e7d32'), (6, '#c62828')]:
    ax_f.plot(ys, f(ys, rv), color=clr, lw=2.4, label=f'$r={rv}$')
ax_f.axhline(0, color='gray', lw=1, alpha=0.6)
ax_f.plot([0, 4], [0, 0], 'o', ms=11, mfc='#888888', mec='black', mew=1.8, zorder=6)
ax_f.plot(2, 0, 'o', ms=11, mfc='#888888', mec='black', mew=1.8, zorder=6)
ax_f.set_xlabel('y', fontsize=12); ax_f.set_ylabel(r'$f(y)=y(4-y)-r$', fontsize=12)
ax_f.set_title(r'$dy/dt$ vs $y$', fontsize=12)
ax_f.legend(fontsize=10, loc='lower center', framealpha=0.92)
ax_f.grid(True, alpha=0.25)
ax_f.set_ylim(-12, 6)

ax_b = fig.add_subplot(gs[:, 2])
r_vals = np.linspace(-8, 4, 300)
y_upper = 2 + np.sqrt(np.clip(4-r_vals, 0, None))
y_lower = 2 - np.sqrt(np.clip(4-r_vals, 0, None))
mask = r_vals <= 4
ax_b.plot(r_vals[mask], y_upper[mask], color='#1b1b1b', lw=3.2, label='Stable branch $y_+$')
ax_b.plot(r_vals[mask], y_lower[mask], color='#1b1b1b', lw=2.4, ls='--', label='Unstable branch $y_-$')
ax_b.plot(4, 2, 'o', ms=13, mfc='#999999', mec='black', mew=2.2, zorder=6, label='Saddle-node pt. $(4,2)$')
ax_b.axvline(4, color='gray', lw=0.8, ls=':', alpha=0.5)
ax_b.annotate('No real equilibria\nfor $r>4$', xy=(0.2, 5.6), fontsize=10, color='#555', style='italic')
ax_b.set_xlabel('r', fontsize=12); ax_b.set_ylabel(r'Equilibrium $y_e$', fontsize=12)
ax_b.set_title('Bifurcation diagram\n(saddle-node at $r=4$)', fontsize=11.5)
ax_b.set_xlim(-8, 7); ax_b.set_ylim(-3, 7)
ax_b.legend(fontsize=9.5, loc='lower left', framealpha=0.92)
ax_b.grid(True, alpha=0.25)

fig.suptitle(r"Problem 1(c):  $\dfrac{dy}{dt} = y(4-y) - r$", fontsize=14.5, y=1.01)
plt.savefig('differenmtialEquation/images/Q1c_saddlenode.png', dpi=155, bbox_inches='tight')
plt.close()
print("Q1c saved.")