from scipy.signal import butter
from cmath import exp, pi
from math import sin, cos
wc = 1
N = 3

_, p, _ = butter(N, wc, analog=True, output='zpk')
a, b = butter(N, wc, analog=True, output='ba')

for k in range(N):
    phi = (1 + 2*k)/(2*N) + (1/2)
    print(phi)
    # root = 1j*exp(1j*())
    # phi = (pi/2)*(1+(2*k+1)/N)
    # phi = (2*k + N + 1) * (1/(2*N))
    # print(phi)
    # root = cos(phi) + 1j*sin(phi)
    # print(root.real)
    # print('found:', "{:g}".format(root))
    # print('got:  ', "{:g}".format(p[k]))
    # print(complex(round(root.real),round(root.imag)))
    # print('got  :', complex(round(p[k].real),round(p[k].imag)))
    # print('found:', root)
    # print('got:', p[k])

# print()
# for k in range(N):
#     print(complex(round(p[k].real),round(p[k].imag)))
# print()