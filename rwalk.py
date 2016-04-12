import numpy as np
import matplotlib as mplt
import matplotlib . pyplot as plt

def rwalk1d (N , p ):

	s = 0

	for i in range ( N ):
			
		r = np . random . random ()
			
		if r > p :
			
			s = s + 1
			
		else :
			
			s = s - 1
			
	return s

n= 100
N = 1000
q=0.5,0.7,0.3

# Aca error 

for i in range(n):

	n0= N/50
	n1 = n0 + i
	n = i


	print n, np.random.random()



	
