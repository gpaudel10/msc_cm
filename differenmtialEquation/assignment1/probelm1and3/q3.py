from differenmtialEquation.assignment1.probelm1and3.helpers import *
from scipy.integrate import solve_ivp

def f(y): return y**3 - 2*y**2 - y + 2   # = (y+1)(y-1)(y-2)

eqs = [-1, 1, 2]

fig = plt.figure(figsize=(16.5, 5.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.3], wspace=0.32)

ax_p = fig.add_subplot(gs[0])
phase_line_panel(ax_p, f, eqs, (-2.5, 3.2), label='Phase line')

ax_f = fig.add_subplot(gs[1])
fy_plot_panel(ax_f, f, eqs, (-2.2, 3.0), label=r'$dy/dt$ vs $y$', ylab=r'$f(y)=y^3-2y^2-y+2$')
legend_proxy(ax_f)

ax_s = fig.add_subplot(gs[2])
t_q = np.linspace(0, 6, 18)
y_q = np.linspace(-2.3, 3.0, 22)
T, Y = np.meshgrid(t_q, y_q)
DT = np.ones_like(T)
DY = f(Y)
mag = np.sqrt(DT**2 + DY**2)
ax_s.quiver(T, Y, DT/mag, DY/mag, color='#999999', alpha=0.55, scale=30,
            headwidth=2, headlength=2.5, headaxislength=2, width=0.0028)

def rhs(t, y): return [f(y[0])]
def event_blowup(t, y): return abs(y[0]) - 25
event_blowup.terminal = True

y0_list = [-1.9, -1.05, -0.3, 0.5, 1.5, 1.9, 2.1, 2.6]
colors  = ['#7b1fa2', '#c62828', '#1565c0', '#1565c0',
           '#1565c0', '#1565c0', '#c62828', '#7b1fa2']

for y0, clr in zip(y0_list, colors):
    sol = solve_ivp(rhs, [0, 6], [y0], max_step=0.01, events=event_blowup, dense_output=True)
    ax_s.plot(sol.t, sol.y[0], color=clr, lw=2.0)

for ye in eqs:
    kind = classify(f, ye)
    mfc = STABLE_C if kind == 'stable' else UNSTABLE_C
    ax_s.axhline(ye, color='black', lw=1.3, ls='--', alpha=0.5)
    ax_s.plot(-0.15, ye, 'o', ms=10, mfc=mfc, mec='black', mew=1.8, zorder=6, clip_on=False)

ax_s.set_xlim(0, 6); ax_s.set_ylim(-2.3, 3.0)
ax_s.set_xlabel('t', fontsize=12); ax_s.set_ylabel('y', fontsize=12)
ax_s.set_title('Slope field with trajectories', fontsize=12)

fig.suptitle(r"Problem 3:  $\dfrac{dy}{dt}=y^3-2y^2-y+2=(y+1)(y-1)(y-2)$", fontsize=14.5, y=1.04)
plt.savefig('differenmtialEquation/images/Q3_cubic_stability.png', dpi=155, bbox_inches='tight')
plt.close()
print("Q3 saved.")