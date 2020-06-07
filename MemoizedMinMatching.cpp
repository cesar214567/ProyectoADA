#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <utility>
#define p 9
#include "Useful.cpp"

using namespace std;

pair<vector<Tupla>, double> cuadA[p][p][p];
pair<vector<Tupla>, double> cuadB[p][p][p];
pair<vector<Tupla>, double> respuestas[p][p]; //inicializar los .second con INT16_MAX;

vector<bloque> A;
vector<bloque> B;

pair<vector<Tupla>, double> min_peso_bloques(int r,int s,int i,int j){
    if (r == s){
        if (cuadA[r][i][j].second==INT16_MAX){
            cuadA[r][i][j].second=0;
            for(int m = i; m <= j; m++) {
                cuadA[r][i][j].first.emplace_back( r, m );
                cuadA[r][i][j].second += B[m].longitud;
            }
        }
        return make_pair ( cuadA[r][i][j].first , A[r].longitud/cuadA[r][i][j].second );

    
    }
    else if (i == j){
        if (cuadB[i][r][s].second ==INT16_MAX){
            cuadB[i][r][s].second=0;
            for(int m = r; m <= s; m++) {
                cuadB[i][r][s].first.emplace_back( m, i );
                cuadB[i][r][s].second += B[m].longitud;
            }
        }
        return make_pair ( cuadB[i][r][s].first , A[r].longitud/cuadB[i][r][s].second );
    }
    else{
		
		double min_resultk = INT16_MAX;
        double min_resultl = INT16_MAX;

        double resultk, resultl;

        pair<vector<Tupla>,double> leftk;
        pair<vector<Tupla>,double> rightk;

        pair<vector<Tupla>,double> leftl;
        pair<vector<Tupla>,double> rightl;

        vector<Tupla> matchsk;
        vector<Tupla> matchsl;
		
        for(int k = j-1; k >=i ; k--){
            auto aux_leftk = min_peso_bloques(r, r, i, k);
            auto aux_rightk = min_peso_bloques(r+1, s, k+1, j);
            resultk  = aux_leftk.second + aux_rightk.second;
            if (min_resultk > resultk ) {
                min_resultk = resultk;
                leftk = aux_leftk;
                rightk = aux_rightk;
            }
        }

        matchsk.insert( matchsk.begin(), begin(leftk.first), end(leftk.first) );
        matchsk.insert( matchsk.end(), begin(rightk.first), end(rightk.first) );

        for(int l = s-1; l >= r ; l--) {
            auto aux_leftl = min_peso_bloques(r, l, i, i);
            auto aux_rightl = min_peso_bloques(l + 1, s, i + 1, j);
            resultl = aux_leftl.second + aux_rightl.second;
            
            if (min_resultl > resultl) {
                min_resultl = resultl;
                leftl = aux_leftl;
                rightl = aux_rightl;

            }
        }

        matchsl.insert( matchsl.begin(), begin(leftl.first), end(leftl.first) );
        matchsl.insert( matchsl.end(), begin(rightl.first), end(rightl.first) );

        if( min_resultk > min_resultl ) {
            respuestas[i][j].first=matchsl;
            respuestas[i][j].second=min_resultl;
        }else{
            respuestas[i][j].first=matchsk;
            respuestas[i][j].second=min_resultk;
        }
        return respuestas[i][j];
    }
}

pair<vector<Tupla>, double> MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  return min_peso_bloques( 0,A.size()-1, 0,B.size()-1) ;
}

int main() {
  
    vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0};
    vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1};
	
	for(int i = 0 ; i < p ; i++){
		for(int j = 0; j < p ; j++){
			respuestas[i][j].second = INT16_MAX;
			for(int k = 0; k < p ; k++){
				cuadA[i][j][k].second = INT16_MAX;
				cuadB[i][j][k].second = INT16_MAX;
			}
		}
	}
    
    auto result = MIN_MATCHING(a,b);

    cout << "Optimo: " << result.second << endl;
    for(auto v : result.first){
        cout<<"("<<v.first<<","<<v.second<<") ";
    }
  
}

