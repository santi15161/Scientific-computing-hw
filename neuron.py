# Santiago Quintana
# trabajo neurona
# 29/03/2016

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

T = 6.3
Phi = 3**(T-6.3)/10, 1 in projects
Delta = 0.001
V = -65




An = phi(0.01(V + 10)/(exp((V + 10)/10)-1))
AM = phi(0.01(V + 25)/(exp((V + 25)/10)-1))
AH = phi(0.07 exp (V/20))
BN = phi(0.125 exp (V/80))
BM = phi(4 exp (V/18))
BH = phi(1/(exp((V + 30)/10)+1))












from scipy.interpolate import interpold

# generates the data

x = np.linspace (0,10,num=10,endpoint=True)
y = np.cos(-x**2 / 9.0)
f = interpld (x,y,kind="Cubic")

# evaluates
print f(0.2)

