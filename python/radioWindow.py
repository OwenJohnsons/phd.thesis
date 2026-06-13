#%%
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')

c = 3e8  # m/s

wavelength, atom_frac = np.loadtxt(
    'atomosphericReflection.dat',
    skiprows=1,
    delimiter='\t',
    unpack=True
)

order = np.argsort(wavelength)
wavelength = wavelength[order]
atom_frac = atom_frac[order]

tick_wavelengths = [
    1e2, None,
    1, 10, 1e-2, 1e-3, 100e-6, None,
    1e-6, 1e-7, 1e-8, None,
    1e-10
]

wave_labels = [
    r'$10^2$ m', '',
    '1 m', '10 m', '1 cm', '1 mm', r'100 $\mu$m', '',
    r'1 $\mu$m', r'0.1 $\mu$m', r'$10^{-2}$ $\mu$m', '',
    r'$\AA$'
]

def freq_label(lam):
    if lam is None:
        return ''

    nu = c / lam

    if nu >= 1e18:
        return rf'{nu/1e18:.0f} EHz'
    elif nu >= 1e15:
        return rf'{nu/1e15:.0f} PHz'
    elif nu >= 1e12:
        return rf'{nu/1e12:.0f} THz'
    elif nu >= 1e9:
        return rf'{nu/1e9:.0f} GHz'
    elif nu >= 1e6:
        return rf'{nu/1e6:.0f} MHz'
    elif nu >= 1e3:
        return rf'{nu/1e3:.0f} kHz'
    else:
        return rf'{nu:.0f} Hz'

freq_labels = [freq_label(lam) for lam in tick_wavelengths]

tick_labels = [
    f'{w}\n{f}' if w else ''
    for w, f in zip(wave_labels, freq_labels)
]

xpos = np.arange(len(tick_wavelengths))

valid = np.array([
    i for i, lam in enumerate(tick_wavelengths)
    if lam is not None
])

log_tick_wavelengths = np.log10([
    tick_wavelengths[i] for i in valid
])

x_valid = xpos[valid]

# Map real wavelength values onto your custom equally spaced axis.
x_equal = np.interp(
    np.log10(wavelength),
    log_tick_wavelengths[::-1],
    x_valid[::-1]
)

fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(x_equal, atom_frac, color='k', label='Atmospheric Reflection')

ax.set_xticks(xpos)
ax.set_xticklabels(tick_labels)

ax.set_xlim(xpos.min(), xpos.max())
ax.set_ylim(0, -9)
ax.invert_yaxis()

# set y ticks 
y_ticks = [0, -1, -2, -3, -4, -5, -6, -7, -8]
ax.set_yticks(y_ticks)
# ax.set_xlabel('Wavelength\nFrequency equivalent')

# Optical region: 1 micron to 0.1 micron
optical_bounds = [1e-6, 1e-7]
optical_x = np.interp(
    np.log10(optical_bounds),
    log_tick_wavelengths[::-1],
    x_valid[::-1]
)

# ax.axvspan(
#     optical_x[0],
#     optical_x[1],
#     color='grey',
#     alpha=0.3,
#     label='Optical Region'
# )

ax2 = ax.twinx()
ax2.set_ylim(0, 140)
ax2.set_ylabel('Altitude (km)')

# ax.legend(loc='best')

plt.tight_layout()
# plt.show()
plt.savefig('atmospheric_reflection.svg')
# %%