
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 7))

# Direction / slope field
T_q = np.linspace(-25, 95, 22);  t_q = np.linspace(0, 90, 22)
T_m, t_m = np.meshgrid(T_q, t_q)
dT = -0.05*(T_m - 20);  dt_ = np.ones_like(dT)
mag = np.sqrt(dt_**2 + dT**2)
ax.quiver(t_m, T_m, dt_/mag, dT/mag, scale=32, alpha=0.38, color='gray')

# Solution curves
t_s = np.linspace(0, 90, 2000)
for T0, color, label in [
    (85, 'steelblue', 'T0=85C (cooling)'),
    (-15,'crimson',   'T0=-15C (warming)'),
]:
    ax.plot(t_s, 20 + (T0-20)*np.exp(-0.05*t_s), color=color, lw=2, label=label)

ax.axhline(20, color='green', ls='--', lw=2, label='T*=20C (stable)')
ax.set(xlabel='Time t (min)', ylabel='T(t) (deg C)')
ax.legend(); ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig('differenmtialEquation/images/Q7_cooling.png', dpi=150)