import numpy as np
import matplotlib.pyplot as plt

Fs=2000
tstep=1/Fs
f0=100

N=int(Fs/f0)

t=np.linspace(0,(N-1)*tstep,N)
fstep=Fs/N
f=np.linspace(0,(N-1)*tstep,N)

y=1*np.sin(2*np.pi*f0*t)


#fft
X=np.fft.fft(y)
X_mag=np.abs(X)/N


#plot
fig,[ax1,ax2]=plt.subplots(nrows=2,ncols=1)
ax1.plot(t,y,'.-')
ax2.plot(f,X_mag,'.-')
plt.show()