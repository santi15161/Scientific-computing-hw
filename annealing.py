import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math

solution = 100

x = np.linspace (-3, 3,solution)

def cost(solution):

	# x=np.linspace(-3, 3,solution)

	l= np.exp(-(x-1)**2)* np.sin(8*x) + 1
	return l

# plt.plot(cost(solution))

plt.plot (x, cost(solution))
plt.show ()


def neighbor (solution):

	step_size = 1.0

	return (2* np.random.random() -1)* step_size + solution


T= 1
Tmin=10**-5

c = np.random.uniform(-3,3,solution)
c1 = neighbor(solution)

