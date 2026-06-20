from differenmtialEquation.assignment1.probelm1and3.helpers import *

def f(y, r): return r*y - y**3

fig = plt.figure(figsize=(16.5, 7.6))
gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1.3],
                       hspace=0.75, wspace=0.32)

ax_p1 = fig.add_subplot(gs[0, 0])
ax_p2 = fig.add_subplot(gs[1, 0])
ax_p3 = fig.add_subplot(gs[2, 0])
phase_line_panel(ax_p1, lambda y: f(y, -1), [0],        (-2.2, 2.2), label=r'$r=-1<0$ (one equilibrium)')
phase_line_panel(ax_p2, lambda y: f(y, 0),  [0],        (-2.2, 2.2), label=r'$r=0$ (degenerate pt.)')
phase_line_panel(ax_p3, lambda y: f(y, 1),  [-1, 0, 1], (-2.2, 2.2), label=r'$r=1>0$ (three equilibria)')

ax_f = fig.add_subplot(gs[:, 1])
ys = np.linspace(-2.2, 2.2, 500)
for rv, clr in [(-1, '#1565c0'), (0, '#2e7d32'), (1, '#c62828')]:
    ax_f.plot(ys, f(ys, rv), color=clr, lw=2.4, label=f'$r={rv}$')
ax_f.axhline(0, color='gray', lw=1, alpha=0.6)
ax_f.plot(0, 0, 'o', ms=11, mfc='#888888', mec='black', mew=1.8, zorder=6)
ax_f.plot([-1, 1], [0, 0], 'o', ms=11, mfc='#1b1b1b', mec='black', mew=1.8, zorder=6)
ax_f.set_xlabel('y', fontsize=12); ax_f.set_ylabel(r'$f(y)=ry-y^3$', fontsize=12)
ax_f.set_title(r'$dy/dt$ vs $y$', fontsize=12)
ax_f.legend(fontsize=10, loc='lower right', framealpha=0.92)
ax_f.grid(True, alpha=0.25)
ax_f.set_ylim(-4, 4)

ax_b = fig.add_subplot(gs[:, 2])
r_neg = np.linspace(-3, 0, 100)
r_pos = np.linspace(0, 3, 150)
ax_b.plot(r_neg, np.zeros_like(r_neg), color='#1b1b1b', lw=3.2, label='Stable')
ax_b.plot(r_pos, np.zeros_like(r_pos), color='#1b1b1b', lw=2.4, ls='--', label='Unstable')
ax_b.plot(r_pos, np.sqrt(r_pos), color='#1b1b1b', lw=3.2)
ax_b.plot(r_pos, -np.sqrt(r_pos), color='#1b1b1b', lw=3.2)
ax_b.plot(0, 0, 'o', ms=12, mfc='#1b1b1b', mec='black', mew=2, zorder=6, label='Pitchfork pt. $(0,0)$')
ax_b.axvline(0, color='gray', lw=0.8, ls=':', alpha=0.5)
ax_b.annotate(r'$y=\sqrt{r}$', xy=(1.7, 1.55), fontsize=10)
ax_b.annotate(r'$y=-\sqrt{r}$', xy=(1.55, -1.8), fontsize=10)
ax_b.set_xlabel('r', fontsize=12); ax_b.set_ylabel(r'Equilibrium $y_e$', fontsize=12)
ax_b.set_title('Bifurcation diagram\n(supercritical pitchfork at $r=0$)', fontsize=11.5)
ax_b.set_xlim(-3, 3.3); ax_b.set_ylim(-2, 2)
ax_b.legend(fontsize=9.5, loc='upper left', framealpha=0.92)
ax_b.grid(True, alpha=0.25)

fig.suptitle(r"Problem 1(d):  $\dfrac{dy}{dt} = r\,y - y^3$", fontsize=14.5, y=1.01)
plt.savefig('differenmtialEquation/images/Q1d_pitchfork.png', dpi=155, bbox_inches='tight')
plt.close()
print("Q1d saved.")