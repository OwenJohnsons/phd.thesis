#%%
import numpy as np
import matplotlib.pyplot as plt
import scienceplots; plt.style.use(['science', 'ieee'])


t = np.linspace(0, 1, 1000)

betas_deg = [0, 15, 30, 45]

fig, axes = plt.subplots(1, 4, figsize=(16, 8))
i = 0 

for ax, beta_deg in zip(axes.flat, betas_deg):

    beta = np.radians(beta_deg)

    a = 1
    b = np.tan(beta)

    x = a * np.cos(2*np.pi*t)
    y = b * np.sin(2*np.pi*t)

    ax.plot(x, y, lw=2)
    ax.set_title(rf'$\beta = {beta_deg}^\circ$')
    ax.set_xlabel(r'$E_a$')
    if i == 0:
        ax.set_ylabel(r'$E_b$')
    ax.set_aspect('equal')
    ax.grid(True)
    
    if i > 0:
        ax.set_yticklabels([])

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    i += 1

plt.tight_layout()
plt.savefig('../chapter2/figures/plane_wave_polarization.pdf')
plt.show()
# %%
