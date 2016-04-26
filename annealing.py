import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math

sulution = 100

def cost(solution):

	x = np.linspace (-3,3,sulution)
	y = np.linspace (0,2,sulution)

	return np.exp(-(x-1)**2)* np.sin((8*x) + 1)
 
plt.plot (cost(sulution))
plt.show ()





def neighbor (solution):

	step_size = 1.0

	return (2* np.random.random() -1)* step_size + solution

T= 1
Tmin=10**-5



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
