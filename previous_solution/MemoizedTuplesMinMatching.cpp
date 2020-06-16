#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <iomanip>
#include <utility>

using namespace std;
#include "Useful.cpp"

vector<vector<pair<double,vector<Tupla>>>> Matrix;

vector<bloque> A;
vector<bloque> B;

pair<double,vector<Tupla>> GetWeightMatchDivision(int i, int m, int n){
	vector<Tupla> retorno;
  double suma = 0.0;
	for(int p = m; p <= n; p++){
		suma += B[p].longitud;
    retorno.emplace_back(Tupla(i,p));
	}

	return make_pair(double(A[i].longitud)/double(suma),retorno);
}
pair<double,vector<Tupla>> GetWeightMatchGroup(int r, int s, int j){
	double suma = 0.0;
  vector<Tupla> retorno;
	for(int p = r; p <= s; p++){
		suma += A[p].longitud;
    retorno.emplace_back(Tupla(p,j));
	}
	return  make_pair(double(suma)/double(B[j].longitud),retorno);
}


pair<double,vector<Tupla>>  min_peso_bloques(int i, int j){
	if(Matrix[i][j].first != 0) {
		return Matrix[i][j];
	}else if ( i == 0 ){
	    Matrix[i][j] = GetWeightMatchDivision(i,0,j);
    }else if ( j == 0 ){
	    Matrix[i][j] = GetWeightMatchGroup(0,i,j);
	}else{
		auto min_resultk = make_pair(double(INT16_MAX),vector<Tupla>());
    auto  min_resultl = make_pair(double(INT16_MAX),vector<Tupla>());

        for(int k = i-1; k >= 0 ; k--){
            auto WeightMatch = GetWeightMatchGroup(k+1,i,j);
            auto SubProblem = min_peso_bloques(k,j-1);
            double result  = WeightMatch.first + SubProblem.first;
            if (min_resultk.first > result){
                min_resultk.first = result;
                min_resultk.second = SubProblem.second;
                min_resultk.second.insert( min_resultk.second.end(), WeightMatch.second.begin(),WeightMatch.second.end() );
            }

        }
        for(int l = j-1; l >= 0 ; l--) {
            auto WeightMatch = GetWeightMatchDivision(i,l+1,j);
            auto SubProblem = min_peso_bloques(i-1,l);
            double result = WeightMatch.first + SubProblem.first;
            if (min_resultl.first > result){
              min_resultl.first = result;
              min_resultl.second = SubProblem.second;
                min_resultl.second.insert( min_resultl.second.end(), WeightMatch.second.begin(),WeightMatch.second.end() );
            }
                

        }
		
		if(min_resultk.first > min_resultl.first){
			Matrix[i][j] = min_resultl;
		}
		else{
			Matrix[i][j] = min_resultk;
		}
	}
    return Matrix[i][j];
}

pair<double,vector<Tupla>> MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  Matrix.resize(A.size());
  
  for(int i = 0; i < A.size(); i++){
	  Matrix[i].resize(B.size());
  }
  vector<Tupla> temp;
  temp.emplace_back(Tupla(0,0));
  Matrix[0][0] = make_pair(A[0].longitud/double(B[0].longitud),temp);
  
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
		  cout<<setw(10)<<Matrix[i][j].first;
	  }
	  cout<<endl;
	}

    cout << "Optimo: " << result.first << endl;
    cout << "Tupla: ";
    for (auto it:result.second){
      cout<<"("<<it.first<<","<<it.second<<") ";
    }
}