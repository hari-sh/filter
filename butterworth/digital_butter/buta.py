import numpy as np 
from scipy import signal 
from math import log10

f_sample = 40000
f_pass = 4000
f_stop = 8000
g_pass = 0.5
g_stop = 40
Td = 1
fs = 0.5

wp = f_pass/(f_sample/2) 
ws = f_stop/(f_sample/2) 
omega_p = (2/Td)*np.tan(wp/2) 
omega_s = (2/Td)*np.tan(ws/2) 

N, Wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog=True) 

print("Order of the Filter=", N)
print("Cut-off frequency= {:.3f} rad/s ".format(Wn)) 

b, a = signal.butter(N, Wn, 'low', True)
z, p = signal.bilinear(b, a, fs) 
# w, h = signal.freqz(z, p, 512)
