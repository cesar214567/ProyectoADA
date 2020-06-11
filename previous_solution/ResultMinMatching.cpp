#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

#include "Useful.cpp"

using namespace std;

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

        for(int k = i; k <= j-1 ; k++){
            auto left = min_peso_bloques(r, r, i, k);
            auto rigth = min_peso_bloques(r+1, s, k+1, j);
            auto res1  = left + rigth;
            if (min_resultk > res1)
                min_resultk = res1;
        }
        for(int l = r; l <= s-1 ; l++) {
            auto left = min_peso_bloques(r, l, i, i);
            auto rigth = min_peso_bloques(l + 1, s, i + 1, j);
            auto res2 = left + rigth;
            if (min_resultl > res2)
                min_resultl = res2;
        }
        return min(min_resultk,min_resultl);
    }
}

double MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  return min_peso_bloques( 0,A.size()-1, 0,B.size()-1) ;
}


int main() {
	vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 };
    vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 };
    
    auto result = MIN_MATCHING(a,b);

    cout << "Optimo: " << result << endl;
}
