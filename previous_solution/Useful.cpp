#include <vector>
using namespace std;
class bloque{
public:
    int longitud;
    int start;
    int end;
    bloque(int start_,int end_, int longitud_):start{start_}, end{end_},longitud{longitud_}{} 
    bloque(int l): longitud{l}{}
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
	bool c = false; 
	for(int i = 0; i < array.size() ; i++){
		if(array[i]){
			cont++; c = true;
			if(i == array.size()-1) v.emplace_back(bloque(i-cont+1,i,cont));  
		}
		else if(cont){
			v.emplace_back(bloque(i-cont,i-1,cont));
			cont = 0; c = false;
		} 
	}
}

void Cargar_consola( vector <int> a ,vector <int> b ){
	
	int p,val; 
	cout << "Ingrese el tamaño del los arrays de 0 y 1 : " ;
	cin >> p; 
	
	cout << "Ingrese elementos de array \"B\" "; 
	for(int i = 0; i < p ; i ++){
		cin >> val;
		a.push_back(val);
	}
	cout << "Ingrese elementos de array \"B\" "; 
	for(int i = 0; i < p ; i ++){
		cin >> val;
		a.push_back(val);
	}
	return;
}