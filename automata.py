import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math

n = 100
np.zeros(0)
w = np.zeros([n, n], dtype = np.int8)

def nextDirection (d, c):
	
	if d == 0:
		c = east 
		print east 

	if d == 1:
		c = south 
		print south 

	if d == 2:
		c = west 
		print west

	if d == 3:
		c = north 
		print north 

	return d

def forward (i, j, d):
	
	return 

def validindex (i, j, n):

	return 

i = n/2 
d = 0

	
for i in range(20000):

	print 


plt.imshow(w, interpolation='none', cmap= plt.cm.Greys, extent=(0,n,0,n))
