#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

#include "Useful.cpp"

using namespace std;

vector<bloque> A;
vector<bloque> B;

double GetWeightMatchDivision(int i, int m, int n){
	double suma = 0.0;
	for(int p = m; p <= n; p++){
		suma += B[p].longitud;
	}
	return A[i].longitud/suma;
}
double GetWeightMatchGroup(int r, int s, int j){
	double suma = 0.0;
	for(int p = r; p <= s; p++){
		suma += A[p].longitud;
	}
	return suma/B[j].longitud;
}


double min_peso_bloques(int i, int j){
    if ( i == 0 ){ 
		return GetWeightMatchDivision(i,0,j);
    }else if ( j == 0 ){ 
		return GetWeightMatchGroup(0,i,j);
    }else{
        double min_resultk = INT16_MAX;
        double min_resultl = INT16_MAX;

        for(int k = i-1; k >= 0 ; k--){
            double WeightMatch = GetWeightMatchGroup(k+1,i,j);
            double SubProblem = min_peso_bloques(k,j-1);
            double result  = WeightMatch + SubProblem;
            if (min_resultk > result)
                min_resultk = result;
        }
        for(int l = j-1; l >= 0 ; l--) {
            double WeightMatch = GetWeightMatchDivision(i,l+1,j);
            double SubProblem = min_peso_bloques(i-1,l);
            double result = WeightMatch + SubProblem;
            if (min_resultl > result)
                min_resultl = result;
        }
        return min(min_resultk,min_resultl);
    }
}

double MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  return min_peso_bloques( A.size()-1, B.size()-1 ) ;
}


int main() {
	vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 };
    vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 };
    
    auto result = MIN_MATCHING(a,b);

    cout << "Optimo: " << result << endl;
}
