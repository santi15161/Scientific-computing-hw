# Santiago Quintana
# trabajo neurona
# 29/03/2016

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

T = 6.3
phi = 3**(T-6.3)/10
delta = 0.001
V = -65

n= 0.317
m= 0.05
h= 0.6

gK = 36
gNa = 120
gL = 0.3

VK= -77
VNa= 50
VL= -54.4

Cm = 0.1
I = 15
Ik = gK** (n**4) * (V-VK)
IL = gL*(V-VL)
INa = gNa * (m**3) * h * (V-VNa)



Alpha_n = phi * (0.01 * (V + 10)/(np.exp((V + 10)/10)-1))
Alpha_M = phi * (0.01 * (V + 25)/(np.exp((V + 25)/10)-1))
Alpha_H = phi * (0.07 * np.exp(V/20))
Beta_N = phi * (0.125 * np.exp (V/80))
Beta_M = phi * (4 * np.exp(V/18))
Beta_H = phi * (1/(np.exp((V + 30)/10)+1))



def f1(asd1):
	asd1 = Alpha_n*(1-n)-Beta_n*n
	return  asd1

def f2(asd2):
	asd2 = Alpha_m*(1-m)-Beta_m*m
	return asd2

def f3(asd3):
	asd3 = Alpha_h*(1-h)- Beta_h*h
	return asd3






# = (I-gK**(n**4)(V-VK)- gNa*m**3*h*(V-VNa)-gL(V-VL))/Cm



#  from scipy.interpolate import interp1d
#
#  # generates the data
#
#  x = np.linspace (0,10,num=10,endpoint=True)
#  y = np.cos(-x**2 / 9.0)
#  f = interp1d (x,y,kind="Cubic")
#
#  # evaluates
#  print f(0.2)

