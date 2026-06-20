import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
warnings.filterwarnings('ignore')

mpl.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 11,
    'mathtext.fontset': 'dejavuserif',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

STABLE_C   = '#1b1b1b'
UNSTABLE_C = 'white'
SEMI_C     = '#999999'
POS_ARROW  = '#1565c0'
NEG_ARROW  = '#c62828'


def classify(f, ye, eps=1e-4):
    left, right = f(ye - eps), f(ye + eps)
    if left > 0 and right < 0:
        return 'stable'
    elif left < 0 and right > 0:
        return 'unstable'
    else:
        return 'semi'


def phase_line_panel(ax, f, eqs, ylim, label=None):
    y0 = 0.5
    eqs = sorted(eqs)
    bounds = [ylim[0]] + eqs + [ylim[1]]
    signs = []
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        if b - a < 1e-9:
            signs.append(signs[-1] if signs else 1)
            continue
        mid = (a + b) / 2
        val = f(mid)
        signs.append(1 if val > 0 else -1)
        pad = 0.10 * (b - a)
        xs, xe = a + pad, b - pad
        if val > 0:
            ax.annotate('', xy=(xe, y0), xytext=(xs, y0),
                         arrowprops=dict(arrowstyle='-|>', lw=2.6, color=POS_ARROW))
        else:
            ax.annotate('', xy=(xs, y0), xytext=(xe, y0),
                         arrowprops=dict(arrowstyle='-|>', lw=2.6, color=NEG_ARROW))
    ax.axhline(y0, color='black', lw=1.6, zorder=1, xmin=0.0, xmax=1.0)
    for idx, ye in enumerate(eqs):
        left_sign, right_sign = signs[idx], signs[idx + 1]
        if left_sign > 0 and right_sign < 0:
            mfc, mew = STABLE_C, 2
        elif left_sign < 0 and right_sign > 0:
            mfc, mew = UNSTABLE_C, 2.6
        else:
            mfc, mew = SEMI_C, 2
        ax.plot(ye, y0, 'o', ms=17, mfc=mfc, mec='black', mew=mew, zorder=5)
        ax.annotate(f'{ye:g}', xy=(ye, y0), xytext=(ye, y0 - 0.30),
                    ha='center', va='top', fontsize=11.5, fontweight='bold')
    ax.set_xlim(ylim)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel('y', fontsize=11.5)
    if label:
        ax.set_title(label, fontsize=11.5)
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)


def fy_plot_panel(ax, f, eqs, ylim, label=None, n=500, ylab='dy/dt = f(y)'):
    ys = np.linspace(ylim[0], ylim[1], n)
    fs = np.array([f(yy) for yy in ys])
    ax.plot(ys, fs, color='#2c3e50', lw=2.4)
    ax.axhline(0, color='gray', lw=1, ls='-', alpha=0.6)
    ax.axvline(0, color='gray', lw=0.7, ls=':', alpha=0.4)
    for ye in sorted(eqs):
        kind = classify(f, ye)
        mfc = STABLE_C if kind == 'stable' else (UNSTABLE_C if kind == 'unstable' else SEMI_C)
        ax.plot(ye, 0, 'o', ms=11, mfc=mfc, mec='black', mew=1.8, zorder=5)
    ax.set_xlabel('y', fontsize=11.5)
    ax.set_ylabel(ylab, fontsize=11.5)
    if label:
        ax.set_title(label, fontsize=11.5)
    ax.grid(True, alpha=0.25)    
    
def legend_proxy(ax):
    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], marker='o', color='w', mfc=STABLE_C, mec='black', mew=2, ms=11, label='Stable'),
        Line2D([0], [0], marker='o', color='w', mfc=UNSTABLE_C, mec='black', mew=2.4, ms=11, label='Unstable'),
        Line2D([0], [0], marker='o', color='w', mfc=SEMI_C, mec='black', mew=2, ms=11, label='Semi-stable'),
    ]
    ax.legend(handles=handles, loc='upper right', fontsize=9, framealpha=0.92)