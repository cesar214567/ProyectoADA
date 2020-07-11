#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <iomanip>
#include <utility>
#include <time.h>
#include <string.h>

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
			

void ObtenerBloques(vector<bloque>& v, vector<int> array){
	int cont= 0; 
	for(int i = 0; i < array.size() ; i++){
		if(array[i]){
			cont++;
			if(i == array.size()-1) v.emplace_back(bloque(i-cont+1,i,cont));  
		}
		else if(cont){
			v.emplace_back(bloque(i-cont,i-1,cont));
			cont = 0;
		} 
	}
}

void Cargar_consola( vector <int> &a ,vector <int> &b ){
	
	string  a_,b_; 
	cout << "Ingrese el vector A de 0 y 1 : " ;
	cin >> a_;
	cout << "Ingrese el vector B de 0 y 1 : " ;
	cin >> b_; 

	for(int i = 0; i < a_.size(); i++){
		a.push_back(int(a_[i]) - 48);
		b.push_back(int(b_[i]) - 48);
	}
	return;
}

void Cargar_random( vector <int> &a ,vector <int> &b ){
	int p,val; 
	cout << "Ingrese el tamaño del los arrays de 0 y 1 : " ;
	cin >> p; 
	srand (time(NULL));
	for(int i = 0; i < p ; i ++){
		val = rand()%2;
		a.push_back(val);
		val = rand()%2;
		b.push_back(val);
	}
    /*
	cout << "El array A: ";
	for(int i = 0; i < p ; i ++){
		cout<< a[i] << " ";
	}
	cout << endl; 
	cout << "El array B: ";
	for(int i = 0; i < p ; i ++){
		cout<< b[i] << " ";
	}
	cout << endl;*/
}

void Menu(vector <int> &a ,vector <int> &b){
	int opcion;
	cout << "Elige una opcion: " << endl;
	cout << "0. Cargar con Consola." <<endl;
	cout << "1. Cargar random." <<endl;
	cout << "2. Salir." <<endl;
	cout << "Ingrese la opcion: ";
	cin >> opcion;
	cout << endl; 
	switch (opcion)
	{
	case 0:
		Cargar_consola(a,b);
		break;
	
	case 1:
		Cargar_random(a,b);
		break;
	 
	case 2: 
		exit(0);
		break;
	}
}

 