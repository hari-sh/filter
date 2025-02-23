import matplotlib.pyplot as plt
from numpy import log10, angle, unwrap, logspace, linspace
from scipy import signal
from cmath import exp
from math import pi
for N in [3,4,5,6,8]:
    poles = []
    zeros = []
    k = 1
    for k in range(N):
        poles.append(1j*exp(1j*pi*(1+2*k)/(2*N)))
    b,a = signal.zpk2tf(zeros,poles,k)
    w,h=signal.freqs_zpk(zeros, poles, k, worN=linspace(0,4,2000))
    plt.plot(w, abs(h))
    plt.grid()
plt.show()