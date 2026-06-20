from differenmtialEquation.assignment1.probelm1and3.helpers import *

K = 4.0
def f(y, r): return r*y*(1 - y/K)

fig = plt.figure(figsize=(15.5, 5.6))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1], width_ratios=[1, 1, 1.3],
                       hspace=0.55, wspace=0.32)

ax_p1 = fig.add_subplot(gs[0, 0])
ax_p2 = fig.add_subplot(gs[1, 0])
phase_line_panel(ax_p1, lambda y: f(y, -1), [0, K], (-2, 6), label=r'Phase line: $r=-1<0$')
phase_line_panel(ax_p2, lambda y: f(y,  1), [0, K], (-2, 6), label=r'Phase line: $r=+1>0$')

ax_f = fig.add_subplot(gs[:, 1])
ys = np.linspace(-2, 6, 400)
ax_f.plot(ys, f(ys, -1), color='#1565c0', lw=2.4, label=r'$r=-1$')
ax_f.plot(ys, f(ys,  1), color='#c62828', lw=2.4, label=r'$r=+1$')
ax_f.axhline(0, color='gray', lw=1, alpha=0.6)
for ye in [0, K]:
    ax_f.plot(ye, 0, 'o', ms=11, mfc='#888888', mec='black', mew=1.8, zorder=6)
ax_f.set_xlabel('y', fontsize=12); ax_f.set_ylabel(r'$f(y)=ry(1-y/K)$', fontsize=12)
ax_f.set_title(r'$dy/dt$ vs $y$  ($K=4$)', fontsize=12)
ax_f.legend(fontsize=9.5, loc='upper right', framealpha=0.92)
ax_f.grid(True, alpha=0.25)
ax_f.axvline(0, color='gray', lw=0.7, ls=':', alpha=0.4)
ax_f.axvline(K, color='gray', lw=0.7, ls=':', alpha=0.4)

ax_b = fig.add_subplot(gs[:, 2])
r_neg = np.linspace(-3, 0, 100); r_pos = np.linspace(0, 3, 100)
ax_b.plot(r_neg, np.zeros_like(r_neg), color='#1b1b1b', lw=3.2)
ax_b.plot(r_pos, np.zeros_like(r_pos), color='#1b1b1b', lw=2.4, ls='--')
ax_b.plot(r_neg, K*np.ones_like(r_neg), color='#1b1b1b', lw=2.4, ls='--')
ax_b.plot(r_pos, K*np.ones_like(r_pos), color='#1b1b1b', lw=3.2)
ax_b.plot(0, 0, 'o', ms=11, mfc='#999999', mec='black', mew=2, zorder=6)
ax_b.plot(0, K, 'o', ms=11, mfc='#999999', mec='black', mew=2, zorder=6)
ax_b.axvline(0, color='gray', lw=0.8, ls=':', alpha=0.5)
ax_b.annotate(r'$y=0$', xy=(2.2, 0.35), fontsize=10)
ax_b.annotate(r'$y=K=4$', xy=(2.2, 4.35), fontsize=10)
ax_b.set_xlabel('r', fontsize=12); ax_b.set_ylabel(r'Equilibrium $y_e$', fontsize=12)
ax_b.set_title('Bifurcation diagram\n(transcritical-type exchange of stability)', fontsize=11.5)
ax_b.set_xlim(-3, 3); ax_b.set_ylim(-1.5, 5.5)
from matplotlib.lines import Line2D
ax_b.legend(handles=[Line2D([0],[0],color='#1b1b1b',lw=3.2,label='Stable'),
                      Line2D([0],[0],color='#1b1b1b',lw=2.4,ls='--',label='Unstable')],
            fontsize=9.5, loc='center left', framealpha=0.92)
ax_b.grid(True, alpha=0.25)

fig.suptitle(r"Problem 1(b):  $\dfrac{dy}{dt} = r\,y\left(1-\dfrac{y}{K}\right),\ K>0$", fontsize=14, y=1.02)
plt.savefig('differenmtialEquation/images/Q1b_logistic.png', dpi=155, bbox_inches='tight')
plt.close()
print("Q1b saved.")