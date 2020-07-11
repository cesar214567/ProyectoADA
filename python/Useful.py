import random 
class bloque:
	def __init__(self,longitud,start,end):
		self.longitud= longitud
		self.start = start
		self.end= end

class tupla: 
	def __init__(self, first,second):
		self.first = first
		self.second = second

def ObtenerBloques(array):
	retorno= []
	cont=0
	for i in range(array):
		if (i):
			cont+=1
			if (i==len(array)-1):
				retorno.append(bloque(i-cont+1,i,cont))
		else:
			if(cont):
				retorno.append(bloque(i-cont,i-1,cont))
				cont=0
	return retorno
			

#void ObtenerBloques(vector<bloque>& v, vector<int> array){
#	int cont= 0; 
#	for(int i = 0; i < array.size() ; i++){
#		if(array[i]){
#			cont++;
#			if(i == array.size()-1) v.emplace_back(bloque(i-cont+1,i,cont));  
#		}
#		else if(cont){
##			v.emplace_back(bloque(i-cont,i-1,cont));
#			cont = 0;
#		} 
#	}
#}

def Cargar_consola(vectorA,vectorB):
	a = str(input("ingrese el vector A de 0 y 1:" ))
	b = str(input("ingrese el vector B de 0 y 1:" ))
	for i in len(a):
		vectorA.append(a[i])
		vectorB.append(b[i])




def Cargar_random(vectorA,vectorB):
	p = int(input("ingrese el tamaño de los arrays de 0 y 1: "))
	for i in range(p):
		vectorA.append(random.random()%2)
		vectorB.append(random.random()%2)
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
		if opcion==2: 
			Cargar_random(vectorA,vectorB)
		else:
			exit(0)



 