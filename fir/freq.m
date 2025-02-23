N = 31;
Nfine = 151;
M = (N - 1)/2
dcycle = 0.4;
w = 2*pi/N*[0:N-1];
A = (w<=dcycle*pi) | (w >= 2*pi -dcycle*pi);
H = A.*exp(-j*M*w);
h = real(ifft(H))
% stem(h)
% figure;
wfine = 2*pi/Nfine * [0: Nfine-1];
Hout = freqz(h, 1, wfine);
plot(wfine, abs(Hout));
hold on;
plot(w, A, 'bo')
hold on;
pause;

