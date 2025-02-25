from scipy import signal
import matplotlib.pyplot as plt
from numpy import abs

b,a=signal.butter(5,1,'low',analog=True)
w,h=signal.freqs(b,a)
plt.figure()
plt.plot(w, abs(h))
# plt.plot(w, np.abs(butterTF(w, N, fCut)), '.')
plt.grid()
plt.show()