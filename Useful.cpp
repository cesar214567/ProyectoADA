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