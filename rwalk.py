import numpy as np
import matplotlib as mplt
import matplotlib . pyplot as plt

n= 100
N =1000
q=0.5,0.7,0.3

def rwalk1d (N , p ):

	s = 0
	for i in range ( N ):			
		r = np.random.random ()			
		if r > p :			
			s = s + 1			
		else :
			s = s - 1
	return s



def f1(N):

	for i in range (100):	
		
		x=rwalk1d(N)

		print x

	return f1(N)

#		n= i
#		ad = N/np.random.random () 



