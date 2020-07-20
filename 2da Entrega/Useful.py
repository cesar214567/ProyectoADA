import random 
import sys
sys.path.append("../Procesamiento")
import pil2 as pil
#from math import floor,ceil
Num_IMG=5

class bloque():
	def __init__(self,start,end,longitud):
		self.longitud= longitud
		self.start = start
		self.end= end

class submatching():
	def __init__(self):
		self.subA=[]
		self.subB=[]
		self.proporcionalidad=[]
	
	def isDivision(self):
		return len(self.subA)==1
	
	def printear(self): 
		print("primer array")

		for i in self.subA:
			print("("+str(i.start)+","+str(i.end)+")",end=" ")
		print("")
		for i in self.subB:
			print("("+str(i.start)+","+str(i.end)+")",end=" ")
		print("")

	def printear2(self):
		print("PROPORCIONALIDADES ")
		for i in self.proporcionalidad:
			print("("+str(i[0])+","+str(i[1])+")")

	def printear3(self):
		print("ultimo bit")
		print(self.subA[len(self.subA)-1].end)
		print(self.subB[len(self.subB)-1].end)


	def getProporcionalidad(self):
		if self.isDivision():
			sumA=float(self.subA[0].longitud)
			sumB=0.0
			k = 0.0
			for i in self.subB:
				sumB+=float(i.longitud)
			for i in self.subB:
				prop =  sumA*(float(i.longitud) /float(sumB))
				rango= [self.subA[0].start + k, self.subA[0].start + k + prop-0.05]
				self.proporcionalidad.append(rango)
				k = k + prop
		else:
			sumB=float(self.subB[0].longitud)
			sumA=0.0
			k=0.0
			for i in self.subA:
				sumA+=float(i.longitud)
			for i in self.subA:
				prop = sumB*(float(i.longitud)/float(sumA))
				rango = [self.subB[0].start + k, self.subB[0].start + k + prop-0.05]
				self.proporcionalidad.append(rango)
				k=k+prop


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
	
def GetSubMatchings(matchings,A,B):
	if len(matchings)==0:
		array_vacio =[]
		return array_vacio
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


def GetAntiMatching(submatchings):
	i,j = 0,0
	antiMatchings = []
	if len(submatchings) == 0:
		Bloque1 = bloque(0,pil.width,pil.width-1)
		Bloque2 = bloque(0,pil.width,pil.width-1)
		subMatch = submatching()
		subMatch.subA.append(Bloque1)
		subMatch.subB.append(Bloque2)
		antiMatchings.append(subMatch)
		return antiMatchings

	for submatch in submatchings:	
		k = submatch.subA[0].start
		l = submatch.subB[0].start	
		if i - k != 0 and j - l != 0:
			Bloque1 = bloque(i,k-1,k-i)
			Bloque2 = bloque(j,l-1,l-j)
			subMatch = submatching()
			subMatch.subA.append(Bloque1)
			subMatch.subB.append(Bloque2)

			antiMatchings.append(subMatch)

		i = submatch.subA[len(submatch.subA)-1].end +1
		j = submatch.subB[len(submatch.subB)-1].end +1 
		
	if i !=pil.width  and j !=pil.width :
		Bloque1 = bloque(i,pil.width,pil.width-1-i)
		Bloque2 = bloque(j,pil.width,pil.width-1-j)
		subMatch = submatching()
		subMatch.subA.append(Bloque1)
		subMatch.subB.append(Bloque2)
		antiMatchings.append(subMatch)

	return antiMatchings


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


