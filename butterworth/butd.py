import matplotlib.pyplot as plt 
from cmath import exp
from math import pi
N = 7
roots = []
for k in range(N):
    roots.append(1j*exp(1j*pi*(1+2*k)/(2*N)))

print(roots)
x = [ele.real for ele in roots] 
y = [ele.imag for ele in roots] 

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
plt.show()