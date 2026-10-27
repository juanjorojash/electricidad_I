import os
import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-1,26,0.01)
i =    (t<0)*0 +\
        ((t>0)&(t<1))*2 +\
        (t>1)*0

v =    (t<0)*0 +\
        ((t>0)&(t<1))*8*(1-np.exp(-(t/5))) +\
        (t>1)*8*(1-np.exp(-(1/5)))*np.exp(-((t-1)/5))

plt.plot(t,i,label=r'$i_f(t)$')
plt.plot(t,v,label=r'$v_c(t)$')
plt.ylim([-1,3])
plt.legend()
plt.show()