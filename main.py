import numpy as np
import matplotlib.pyplot as plt

Fs=2000
tstep=1/Fs
f0=100

N=int(10 * Fs/f0)

t=np.linspace(0,(N-1)*tstep,N)
fstep=Fs/N
f=np.linspace(0,(N-1)*tstep,N)

y=1*np.sin(2*np.pi*f0*t) + 4*np.sin(3*np.pi*3*f0*t)


#fft
x=np.fft.fft(y)
x_mag=np.abs(x)/N

f_plot = f[0:int(N/2+1)]
x_mag_plot = 2 * x_mag[0:int(N/2+1)]
x_mag_plot[0] = x_mag[0] / 2

#plot
fig,[ax1,ax2]=plt.subplots(nrows=2,ncols=1)
ax1.plot(t,y,'.-')
ax2.plot(f_plot,x_mag_plot,'.-')
plt.show()