#!/usr/bin/env python

import numpy as np
import scipy as sp
from scipy import integrate


x = np.arange(0, 2*np.pi, .0000001)

print x

f = lambda x:np.sin(x)

y = f(x)


I = sp.integrate.quad(f,0,2*np.pi)

I2 = sp.integrate.simps(y)


print I
print I2







