from scipy import signal
from math import pi
numtaps = 7
f = 1
h = signal.firwin(numtaps, cutoff=1, window='rect', fs=2*pi)
print(h)
