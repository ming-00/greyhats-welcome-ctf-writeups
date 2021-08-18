from pwn import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys
r = remote('challs1.nusgreyhats.org',5213)
samples = 920        
symb = 10
samples = samples - samples % symb
print(r.recvuntil("Frequency = ").decode('utf-8'))
f = float(r.recvuntil("(")[:-1])
print(f)
r.recvuntil("Total signal time = ")
us = float(r.recvuntil("(")[:-1])
print(us)
r.recvuntil("Input up to 1000 different time (μs) seperated by space :")
r.recvline()
r.sendline(" ".join(str(x / samples * us) for x in range(samples)[:1000]))
r.recvline()
sig = list(map(float, r.recvline().split(b" ")))

sps = 1 / (us * 10**-6 / samples)
print(sps)
#print(sig)
#plt.plot(sig)
#plt.show()

#open('signal','wb').write(b"".join(struct.pack('f', x) for x in sig))
grad = np.gradient(sig)**2

sigfreq = np.abs(np.fft.rfft(grad))
#plt.ion()
#sigfreq[0] = 0
fullcycle = sps / (f*10**6)
print(fullcycle)
loi = np.sin(np.arange(samples) / fullcycle * 2 * np.pi)[:1000]
loq = np.cos(np.arange(samples) / fullcycle * 2 * np.pi)[:1000]

ifi = sig * loi
ifq = sig * loq

x = max(np.argsort(np.abs(np.fft.fft(ifi+1j*ifq)))[-2:])
print(x)
sos = signal.ellip(8, 1, 100, x / 2 - 10, 'lp', fs=samples, output='sos')

#ifi = signal.sosfilt(sos, ifi)
#ifq = signal.sosfilt(sos, ifq)

ifi = np.mean(ifi.reshape(-1, symb), axis=1)
ifq = np.mean(ifq.reshape(-1, symb), axis=1)

#plt.plot(np.abs(np.fft.fft(ifi+1j*ifq)))
plt.plot(ifi)
plt.plot(ifq)
#plt.show()
constellation = [
    ["0000", "0100" , "1100", "1000"]
           ,
 ["0001" ,"0101" , "1101", "1001"]
 ,
 ["0011" ,"0111" , "1111", "1011"]
           ,
 ["0010" ,"0110" , "1110", "1010"]][::-1]

def transform(x):
    xx = []
    for a in x:
        if a < -1:
            xx.append(0)
        elif a < -0:
            xx.append(1)
        elif a < 1:
            xx.append(2)
        else:
            xx.append(3)
    return xx

ifi = transform(ifi)
ifq = transform(ifq)

s = ""
ss = ""
for x, y in zip(ifi, ifq):
    x = min(max(x, 0), 3)
    y = min(max(y, 0), 3)
    s += constellation[y][x]
    if len(s) == 8:
        ss += chr(int(s, 2))
        s = ""
print(ss)
#plt.scatter(ifi, ifq)
#grad = np.gradient(ifi)**2

#sigfreq = np.abs(np.fft.rfft(grad))
#plt.plot(sigfreq)
plt.show()
r.interactive()