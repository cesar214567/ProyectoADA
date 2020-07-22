import random 
import sys
sys.path.append("../Procesamiento")
import pil2 as pil
from math import floor,ceil
import numpy as np

Num_IMG=30

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
				rango= [self.subA[0].start + k, self.subA[0].start + k + prop-0.001]
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
				rango = [self.subB[0].start + k, self.subB[0].start + k + prop-0.001]
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
	if len(matchings)==0 or len(A)==0 or len(B)==0:
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

def generarMatrizPorLinea(matchings,antimatchings,row11,row12):
	matrix= []
	matrix.append(row11)

	# Sacamos el diferencial entre un pixel de la imagen b y uno de la imagen a entre i iteraciones 
	for i in range(Num_IMG-1):
		lista= []
		for j in range(len(row11)):
			init=[]
			R = round(row11[j][0]+ (float(i+1)/float(Num_IMG))* (row12[j][0]-row11[j][0]))
			G = round(row11[j][1]+ (float(i+1)/float(Num_IMG))* (row12[j][1]-row11[j][1]))
			B = round(row11[j][2]+ (float(i+1)/float(Num_IMG))* (row12[j][2]-row11[j][2]))
			init.append((R,G,B))
			lista.append(init)
		matrix.append(lista)
    
	colorearIfMatching(matchings,matrix,row11,row12)
	colorearIfMatching(antimatchings,matrix,row11,row12)
	matrix.append(row12)
	contador=0
	sacar_promedio(matrix,len(row11))
	return matrix

def colorearIfMatching(matchings,matrix,row11,row12):	
	# Agregamos los demas pixeles a la lista 
	for j in range(len(matchings)):
		proporcionalidades=matchings[j].proporcionalidad
		if (matchings[j].isDivision()): 
			for index in range(len(proporcionalidades)):
				inicio1= proporcionalidades[index][0]
				end1 = proporcionalidades[index][1]
				inicio2 =float(matchings[j].subB[index].start)
				end2 =float(matchings[j].subB[index].end)
				tamano_total=ceil(end1)-floor(inicio1)
				#hacer el calculo para cada iteracion
				for k in range(Num_IMG-1):
					initK = inicio1 + (k+1)*(inicio2-inicio1)/float(Num_IMG)
					endK = end1 + (k+1)*(end2-end1)/float(Num_IMG)
					long_pixel_K = (endK-initK)/float(tamano_total)
					for t in np.arange(initK,endK,long_pixel_K):
						rango = long_pixel_K/float(matchings[j].subB[index].longitud)
						cont = floor(inicio2)
						cont2 = t
						for pixel in range(floor(t),ceil(t+long_pixel_K),1):
							if pixel > cont2 + rango: 
								cont = cont + 1
								cont2 = cont2 + rango
							R = round(row11[floor(t)][0] + (float(k+1)/float(Num_IMG))* (row12[cont][0]-row11[floor(t)][0]))
							G = round(row11[floor(t)][1] + (float(k+1)/float(Num_IMG))* (row12[cont][1]-row11[floor(t)][1]))
							B = round(row11[floor(t)][2] + (float(k+1)/float(Num_IMG))* (row12[cont][2]-row11[floor(t)][2]))
							matrix[k+1][pixel].append((R,G,B))
		else:
			for index in range(len(proporcionalidades)):
				inicio1 = float(matchings[j].subA[index].start)
				end1 = float(matchings[j].subA[index].end)
				inicio2 = proporcionalidades[index][0]
				end2 = proporcionalidades[index][1]
				tamano_total= ceil(end2)-floor(inicio2)
				for k in range(Num_IMG-2,0,-1): ##esto va en sentido inverso, de abajo a arriba
					initK = inicio2 +(k+1)*(inicio1-inicio2)/float(Num_IMG)
					endK = end2 + (k+1)*(end1-end2)/float(Num_IMG)
					long_pixel_K = (endK-initK)/float(tamano_total)
					for t in np.arange(initK,endK,long_pixel_K):
						rango = long_pixel_K/float(matchings[j].subA[index].longitud)
						cont = floor(inicio1)
						cont2 = t
						for pixel in range (floor(t),ceil(t+long_pixel_K),1):
							if pixel >cont2+rango:
								cont = cont+1 
								cont2=cont2+rango
							R = round(row11[floor(t)][0] + (float(k+1)/float(Num_IMG))* (row12[cont][0]-row11[floor(t)][0]))
							G = round(row11[floor(t)][1] + (float(k+1)/float(Num_IMG))* (row12[cont][1]-row11[floor(t)][1]))
							B = round(row11[floor(t)][2] + (float(k+1)/float(Num_IMG))* (row12[cont][2]-row11[floor(t)][2]))
							matrix[k+1][pixel].append((R,G,B))
                            
    

    #for i in range(Num_IMG):
    #    for j in range(len(row11)):
    #        print(str(matrix[i][j]),end=" ")
    #    print("")

    
def sacar_promedio(matrix,width):
	for i in range(1,Num_IMG,1):
		for j in range(width):
			sumR = 0
			sumG = 0
			sumB = 0
			for iter in matrix[i][j]:
				sumR = sumR + iter[0]
				sumG = sumG + iter[1]
				sumB = sumB + iter[2]
			sumR = round(sumR/len(matrix[i][j]))
			sumG = round(sumG/len(matrix[i][j]))
			sumB = round(sumB/len(matrix[i][j]))
			matrix[i][j] = (sumR,sumG,sumB,255)





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


