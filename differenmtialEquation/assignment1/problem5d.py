import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: K = 2  ->  y(t) = (2 - cos t)^(-3), defined for all t
t1 = np.linspace(-3*np.pi, 5*np.pi, 15000)
ax1.plot(t1, (2-np.cos(t1))**(-3), lw=2)
ax1.plot(np.pi/2, 1/8, 'ro', ms=9, label='IC (pi/2, 1/8)')
ax1.set(title='K=2: global solution', xlabel='t', ylabel='y')

# Panel 2: K = 1/2 -> blows up at t = pi/3 and t = 5pi/3
t_L, t_R = np.pi/3, 5*np.pi/3
t2 = np.linspace(t_L+1e-4, t_R-1e-4, 30000)
y2 = np.clip((0.5-np.cos(t2))**(-3), -1, 30)
ax2.plot(t2, y2, 'r', lw=2)
ax2.axvline(t_L, color='purple', ls=':', label='Singularity pi/3')
ax2.axvline(t_R, color='orange', ls=':', label='Singularity 5pi/3')
ax2.plot(np.pi/2, 8, 'go', ms=9, label='IC (pi/2, 8)')
ax2.set(title='K=1/2: blowup at pi/3 and 5pi/3', xlabel='t', ylabel='y')

for a in (ax1, ax2):
    a.legend(); a.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig('differenmtialEquation/images/Q5_solutions.png', dpi=150)