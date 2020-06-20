#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <iomanip>
#include <utility>
#include <time.h>
using namespace std;

class bloque{
public:
    int longitud;
    int start;
    int end;
    bloque(int start_,int end_, int longitud_):start{start_}, end{end_},longitud{longitud_}{} 
};

class Tupla{
public:
    int first;
    int second;
    Tupla(int first, int second){
        this->first = first;
        this->second = second;
    }
};

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
	
	int p,val; 
	cout << "Ingrese el tamaño del los arrays de 0 y 1 : " ;
	cin >> p; 
	
	cout << "Ingrese elementos de array \"A\" : "; 
	for(int i = 0; i < p ; i ++){
		cin >> val;
		a.push_back(val);
	}
	cout << "Ingrese elementos de array \"B\" : "; 
	for(int i = 0; i < p ; i ++){
		cin >> val;
		b.push_back(val);
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

 