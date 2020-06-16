#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <iomanip>

#include "Useful.cpp"

using namespace std;

vector<vector<double>> Matrix;

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
	if(Matrix[i][j] != 0) {
		return Matrix[i][j];
	}else if ( i == 0 ){
	    Matrix[i][j] = GetWeightMatchDivision(i,0,j);
    }else if ( j == 0 ){
	    Matrix[i][j] = GetWeightMatchGroup(0,i,j);
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
		
		if(min_resultk > min_resultl){
			Matrix[i][j] = min_resultl;
		}
		else{
			Matrix[i][j] = min_resultk;
		}
	}
    return Matrix[i][j];
}

double MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  Matrix.resize(A.size());
  
  for(int i = 0; i < A.size(); i++){
	  Matrix[i].resize(B.size());
  }
  
  Matrix[0][0] = A[0].longitud/double(B[0].longitud);
  
  return min_peso_bloques( A.size()-1, B.size()-1 ) ;
}


int main() {
	//vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 };
    //vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 };
	//vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1};
    //vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0};
    vector<int>a;
    vector<int>b;
    Cargar_consola(a,b);
    auto result = MIN_MATCHING(a,b);
	
	for(int i = 0; i < A.size(); i++){
	  for(int j = 0; j < B.size(); j++){
		  cout<<setw(10)<<Matrix[i][j];
	  }
	  cout<<endl;
	}

    cout << "Optimo: " << result << endl;
}
