from scipy import signal 
from math import log10, pi
from scipy.signal import cont2discrete
import numpy
numpy.set_printoptions(precision=4, suppress=True)

f_sample = 8000
f_pass = 800
f_stop = 2400
g_pass = -20*log10(0.8)
g_stop = -20*log10(0.2)

wp = f_pass*pi/(f_sample/2) 
ws = f_stop*pi/(f_sample/2)

N, Wn = signal.buttord(wp, ws, g_pass, g_stop, analog=True)
b, a = signal.butter(N, Wn, 'low', analog=True)

digb, diga, _ = cont2discrete((b, a), dt=1, method='impulse')
print('Digital Numerator: ', digb)
print('Digital Denominator: ', diga)