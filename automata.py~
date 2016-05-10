import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math

n = 100
np.zeros(0)
w = np.zeros([n, n], dtype = np.int8)

i = n/2 
j = n/2
d = 0

east = 0
south = 1
west = 2
north = 3

blanco = 0
negro = 1

def nextDirection (d, c):
	
	if c == blanco:

		if d == east:
			d1 = south
		
		if d == south:
			d1 = west
		
		if d == west:
			d1 = north

		if d == north:
			d1 = east

	if c == negro:
	
		if d == east:
			d1 = north
		
		if d == south:
			d1 = east
		
		if d == west:
			d1 = south

		if d == north:
			d1 = west

	return d1

def moveforward (i, j, d):
	
	return 

def validindex (i, j, n):
		# Validar si la posicion sirve o no 
	return 

plt.imshow(w, interpolation='none', cmap= plt.cm.Greys, extent=(0,n,0,n))
