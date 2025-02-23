import matplotlib.pyplot as plt
from numpy import log10, angle, unwrap, logspace, linspace
from scipy import signal
from cmath import exp
from math import pi
N = 4
poles = []
zeros = []
k = 1
for k in range(N):
    poles.append(1j*exp(1j*pi*(1+2*k)/(2*N)))

print(poles)
x = [ele.real for ele in poles] 
y = [ele.imag for ele in poles] 

ax = plt.gca()

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
circ = plt.Circle((0, 0), radius=1, edgecolor='r', facecolor='None', ls='--')
ax.add_patch(circ)

plt.plot(x, y, 'g*')

worN=linspace(start=-1, stop=5, num=100)
# zeros, poles, k = signal.butter(4, 1, output='zpk', fs=4)
w, h = signal.freqs_zpk(zeros, poles, k, worN=worN)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Digital filter frequency response')

ax1.plot(w, 20 * log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [Hz]')
ax1.grid(True)

# ax2 = ax1.twinx()
# phase = unwrap(angle(h))
# ax2.plot(w, phase, 'g')
# ax2.set_ylabel('Phase [rad]', color='g')

# plt.axis('tight')
plt.show()