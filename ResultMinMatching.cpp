#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

class bloque{
public:
    int longitud;
    bloque(int l): longitud{l}{}
};

//A = [ 0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 1 , 0]
//B = [ 0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1]

vector<bloque> A;
vector<bloque> B;

double min_peso_bloques(int r , int s, int i, int j){
    if ( r == s || i == j){
        double sumBloquesA = 0.0;
        double sumBloquesB = 0.0;

        for(int m = r; m <= s; m++) sumBloquesA += A[m].longitud;
        for(int m = i; m <= j; m++) sumBloquesB += B[m].longitud;

        return (sumBloquesA/sumBloquesB);
    }else{
        double min_resultk = INT16_MAX;
        double min_resultl = INT16_MAX;

        for(int k = j-1; k >=i ; k--){
            auto left = min_peso_bloques(r, r, i, k);
            auto rigth = min_peso_bloques(r+1, s, k+1, j);
            auto res1  = left + rigth;
            if (min_resultk > res1)
                min_resultk = res1;
        }
        for(int l = s-1; l >= r ; l--) {
            auto left = min_peso_bloques(r, l, i, i);
            auto rigth = min_peso_bloques(l + 1, s, i + 1, j);
            auto res2 = left + rigth;
            if (min_resultl > res2)
                min_resultl = res2;
        }
        return min(min_resultk,min_resultl);
    }
}


int main() {
    A.emplace_back(bloque(1));
    A.emplace_back(bloque(2));
    A.emplace_back(bloque(1));
    //A.emplace_back(bloque(7));
    //A.emplace_back(bloque(3));
    //A.emplace_back(bloque(6));
    B.emplace_back(bloque(2));
    B.emplace_back(bloque(2));
    B.emplace_back(bloque(1));
    cout << "Optimo: " <<endl <<min_peso_bloques(0,A.size()-1, 0,B.size()-1);
}
