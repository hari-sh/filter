import numpy as np 
from scipy import signal 
from math import log10, pi, tan

f_sample = 8000
f_pass = 800
f_stop = 2400
g_pass = -20*log10(0.8)
g_stop = -20*log10(0.2)
Td = 2
fs = 0.5

wp = f_pass*pi/(f_sample/2) 
ws = f_stop*pi/(f_sample/2) 
omega_p = (2/Td)*tan(wp/2) 
omega_s = (2/Td)*tan(ws/2) 

omrat = omega_s/omega_p

N, Wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog=True) 

print("Order of the Filter=", N)
print("Cut-off frequency= {:.3f} rad/s ".format(Wn)) 

b, a = signal.butter(N, Wn, 'low', True)
digb, diga = signal.bilinear(b, a, fs) 
# w, h = signal.freqz(z, p, 512)
print()