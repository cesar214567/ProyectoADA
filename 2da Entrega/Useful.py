import random 
class bloque():
	def __init__(self,start,end,longitud):
		self.longitud= longitud
		self.start = start
		self.end= end

class submatching():
	def __init__(self):
		self.subA=[]
		self.subB=[]

	def isDivision(self):
		return len(subA)==1
	def printear(self): 
		print("primer array")

		for i in self.subA:
			print(i.longitud,end=" ")
		print("")
		for i in self.subB:
			print(i.longitud,end=" ")
		print("")

def ObtenerBloques(array):
	retorno= []
	cont=0
	iterador=0
	for i in array:
		if (i==1):
			cont+=1
			if (iterador==len(array)-1):
				retorno.append(bloque(iterador-cont+1,iterador,cont))
		else:
			if(cont):
				retorno.append(bloque(iterador-cont,iterador-1,cont))
				cont=0
		iterador+=1
	return retorno

def Cargar_consola(vectorA,vectorB):
	a = str(input("ingrese el vector A de 0 y 1:" ))
	b = str(input("ingrese el vector B de 0 y 1:" ))
	for i in range(len(a)):
		vectorA.append(int(a[i]))
		vectorB.append(int(b[i]))

def Cargar_random(vectorA,vectorB):
	p = int(input("ingrese el tamaño de los arrays de 0 y 1: "))
	for i in range(p):
		vectorA.append(random.randint(0,1))
		vectorB.append(random.randint(0,1))
	print("el array A",vectorA)
	print("el array B",vectorB)


def Menu(vectorA,vectorB):
	print("Elige una opcion: ")
	print("0. Cargar con Consola.")
	print("1. Cargar random.") 
	print("2. Salir." )
	opcion = int(input("Ingrese la opcion: "))
	if opcion==0:
		Cargar_consola(vectorA,vectorB)
	else:
		if opcion==1: 
			Cargar_random(vectorA,vectorB)
		else:
			exit(0)

def GetMatriz(txt):
	matrix = []
	f = open(txt, "r")
	lines = f.readlines()
	for line in lines:
		temp = []
		for i in range(0, len(line)-1):
			temp.append(int(line[i]))
		matrix.append(temp)
	return matrix

def ImprimirMatriz(matrix):
    for it in matrix:
        for it2 in it:
            print(it2, end=' ')
        print("")
    print("")
	
def proporcionaliad(matchings,A,B):
	t_a = matchings[0][0]
	t_b = matchings[0][1]
	submatchings=[]
	SubMatching= submatching()
	SubMatching.subA.append(A[t_a])
	SubMatching.subB.append(B[t_b])
	for i in range  (1,len(matchings),1):
		if(matchings[i][0] == t_a):
			SubMatching.subB.append(B[matchings[i][1]])        
		elif (matchings[i][1] == t_b):
			SubMatching.subA.append(A[matchings[i][0]])
		else:
			submatchings.append(SubMatching)
			SubMatching=submatching()
			t_a = matchings[i][0]
			t_b = matchings[i][1]
			SubMatching.subA.append(A[t_a])
			SubMatching.subB.append(B[t_b])
	submatchings.append(SubMatching)
	return submatchings

if __name__ == "__main__":
	A=[]
	B=[]
	Menu(A,B)	
	bloquesA = ObtenerBloques(A)
	bloquesB = ObtenerBloques(B)
	for i in bloquesA:
		print(str(i.start) +" "+str(i.end) +" "+str(i.longitud))
	print("espacio")
	for i in bloquesB:
		print(str(i.start) +" "+str(i.end) +" "+str(i.longitud)) 


