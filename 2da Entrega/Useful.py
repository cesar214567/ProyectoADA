import random 
class bloque():
	def __init__(self,start,end,longitud):
		self.longitud= longitud
		self.start = start
		self.end= end

def ObtenerBloques(array):
	print(array)
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

if __name__ == "__main__":
	A=[]
	B=[]
	Menu(A,B)
	print(A)
	print(B)	
	bloquesA =ObtenerBloques(A)
	bloquesB = ObtenerBloques(B)
	for i in bloquesA:
		print(str(i.start) +" "+str(i.end) +" "+str(i.longitud))
	print("espacio")
	for i in bloquesB:
		print(str(i.start) +" "+str(i.end) +" "+str(i.longitud)) 

def GetMatriz(txt):
    matriz1 = []
    linea = ''
    imput = open(txt)

    while(imput.readline()):
        temp = []
        for i in range (0, len(linea)):
            temp.append(linea[i]-48)
        matriz1.append(temp)
    return matriz1


