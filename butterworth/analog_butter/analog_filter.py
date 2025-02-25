import numpy as np
from scipy.signal import freqs_zpk, iirfilter

z, p, k = iirfilter(3, 1, btype='lowpass', analog=True, ftype='butter', output='zpk')
w, h = freqs_zpk(z, p, k, worN=np.logspace(-1, 2, 1000))

import matplotlib.pyplot as plt
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude response [dB]')
plt.grid(True)
plt.show()

