import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, zpk2tf, tf2sos, sosfreqz, sos2zpk

# Analog filter, H(s) = 2 / (s^2 + 3s + 2)
b = np.array([2])  # numerator coeff of analog filter
a = np.array([1, 3, 2])  # denominator coeff of analog filter
fs = 1  # sampling frequency

# Impulse invariant transformation
dt = 1/fs
num_d, den_d, _ = cont2discrete((b, a), dt)

# Convert to numerator/denominator form
bz, az = zpk2tf([], np.roots(den_d), num_d)

# Convert to second-order sections form
sos = tf2sos(bz, az)

# Plot frequency response of digital filter H(z)
w, h = sosfreqz(sos)
plt.plot(w/np.pi, np.abs(h))
plt.title('Frequency Response of Low-Pass Filter')
plt.xlabel('Normalized Frequency (x pi rad/sample)')
plt.ylabel('Magnitude')
plt.show()

# Plot zero and poles of the filter
z, p, k = sos2zpk(sos)
plt.plot(np.real(z), np.imag(z), 'o', label='Zeros')
plt.plot(np.real(p), np.imag(p), 'x', label='Poles')
plt.title('Pole-Zero Plot of Low-Pass Filter')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.grid()
plt.show()