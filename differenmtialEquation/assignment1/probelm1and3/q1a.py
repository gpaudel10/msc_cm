from differenmtialEquation.assignment1.probelm1and3.helpers import *

fig = plt.figure(figsize=(15.5, 5.6))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1], width_ratios=[1, 1, 1.3],
                       hspace=0.55, wspace=0.32)

ax_p1 = fig.add_subplot(gs[0, 0])
ax_p2 = fig.add_subplot(gs[1, 0])
phase_line_panel(ax_p1, lambda y: -1*y, [0], (-3, 3), label=r'Phase line: $r=-1<0$')
phase_line_panel(ax_p2, lambda y:  1*y, [0], (-3, 3), label=r'Phase line: $r=+1>0$')

ax_f = fig.add_subplot(gs[:, 1])
ys = np.linspace(-3, 3, 400)
ax_f.plot(ys, -1*ys, color='#1565c0', lw=2.4, label=r'$r=-1$')
ax_f.plot(ys,  1*ys, color='#c62828', lw=2.4, label=r'$r=+1$')
ax_f.axhline(0, color='gray', lw=1, alpha=0.6)
ax_f.axvline(0, color='gray', lw=0.7, ls=':', alpha=0.4)
ax_f.plot(0, 0, 'o', ms=12, mfc='#888888', mec='black', mew=2, zorder=6,
          label=r'$y=0$ (stability flips at $r=0$)')
ax_f.set_xlabel('y', fontsize=12); ax_f.set_ylabel(r'$f(y)=ry$', fontsize=12)
ax_f.set_title(r'$dy/dt$ vs $y$', fontsize=12)
ax_f.legend(fontsize=9, loc='upper left', framealpha=0.92)
ax_f.grid(True, alpha=0.25)

ax_b = fig.add_subplot(gs[:, 2])
r_neg = np.linspace(-3, 0, 100)
r_pos = np.linspace(0, 3, 100)
ax_b.plot(r_neg, np.zeros_like(r_neg), color='#1b1b1b', lw=3.2, label='Stable branch')
ax_b.plot(r_pos, np.zeros_like(r_pos), color='#1b1b1b', lw=2.4, ls='--', label='Unstable branch')
ax_b.plot(0, 0, 'o', ms=12, mfc='#999999', mec='black', mew=2, zorder=6)
ax_b.axvline(0, color='gray', lw=0.8, ls=':', alpha=0.5)
ax_b.set_xlabel('r', fontsize=12); ax_b.set_ylabel(r'Equilibrium $y_e$', fontsize=12)
ax_b.set_title('Bifurcation diagram\n(degenerate / linear stability switch)', fontsize=11.5)
ax_b.set_xlim(-3, 3); ax_b.set_ylim(-1.5, 1.5)
ax_b.legend(fontsize=9.5, loc='upper left', framealpha=0.92)
ax_b.grid(True, alpha=0.25)

fig.suptitle(r"Problem 1(a):  $\dfrac{dy}{dt} = r\,y$", fontsize=14, y=1.02)
plt.savefig('differenmtialEquation/images/Q1a_linear.png', dpi=155, bbox_inches='tight')  
plt.close()
print("Q1a saved.")