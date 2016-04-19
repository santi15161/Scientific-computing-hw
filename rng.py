import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math


np.random.seed(0)


n = 50000
xu = np.random.uniform(-20, 20, n)
xb = np.random.binomial(200, 0.25, n)
xn = np.random.normal(0.0, 10, n)

bins = 30
y1, x1 = np.histogram(xu, bins=bins, density=True)
y2, x2 = np.histogram(xb, bins=bins, density=True)
y3, x3 = np.histogram(xn, bins=bins, density=True)

x1 = x1[0 : -1] + 0.5 * (x1[1] - x1[0])
x2 = x2[0 : -1] + 0.5 * (x2[1] - x2[0])
x3 = x3[0 : -1] + 0.5 * (x3[1] - x3[0])

plt.plot(x1,y1,"b-")
plt.plot(x2,y2,"r-")
plt.plot(x3,y3,"g-")
plt.show()

a = [1,2,3,4,5]
b = sum(a)
print b



# def fun(asd):
#	n= 200
	 






# for i in range():

	# print np.random.random(2)

#	print np.random.uniform(a,b)
#	print np.random.binomial(N,p)
#	print np.random.normal (mu , sigma)
#	print np.histogram (x, bins=<bins>)
