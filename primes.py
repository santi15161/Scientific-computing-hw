
# x = input("Primer Numero: ")
# y = input("Segundo Numero: ")
#
#
# if x<y:
#	print x
# else:
#	print y
#
# El cogdigo anteriormente Nos enseña a pedir al usuario ingresar 2 numeros y imprima el menor





# esta funcion define  si un numero es menor que otro 

def minimo (x,y):
	if x < y:
		return x
	else:
		return y
def mcd (x,y):
	m = minimo (x,y)
	for i in range (m,0,-1):

		if x % i == 0 and y % i == 0:
			return i

# Esta funcion define si un numero es coprimo o no 

def arecoprime (a,b):

	m = mcd (a,b)

	if m==1:
		return 1
	else:
		return 0

print arecoprime (12,16)

















