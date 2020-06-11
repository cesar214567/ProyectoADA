#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <utility>
#include <map>

#include "Useful.cpp"

using namespace std;

vector<bloque> A;
vector<bloque> B;

bool check(vector<Tupla>& matchings){
    Tupla aux = matchings[matchings.size()-1];
    map<pair<int,int>,bool> tuplas;

    for (int i = 0; i < matchings.size() ; ++i) {
        pair<int,int> tupla = make_pair(matchings[i].first,matchings[i].second);
        tuplas.insert(make_pair(tupla,true));
    }

    for(int i = matchings.size()-2; i >= 0 ; i--){
        if(matchings[i].first < aux.first && matchings[i].second < aux.second){
            pair<int,int> aux_1 = make_pair(matchings[i].first,aux.second);
            pair<int,int> aux_2 = make_pair(aux.first,matchings[i].second);
            if(tuplas.find(aux_1) != tuplas.end() || tuplas.find(aux_2)!= tuplas.end()){
                return false;
            }
	    }
    }
    return true;
}

double GetWeight(vector<Tupla>& matchings){

    if(!check(matchings)) return INT16_MAX;

    double Weight = 0.0;

    double sumaBloquesA = A[matchings[0].first].longitud;
    double sumaBloquesB = B[matchings[0].second].longitud;

    double prevIndex_i = matchings[0].first;
    double prevIndex_j = matchings[0].second;

    for (int i = 1 ; i < matchings.size(); i++){
        if( matchings[i].first == prevIndex_i ){ //División
            sumaBloquesB += B[matchings[i].second].longitud;
        }
        else if (matchings[i].second == prevIndex_j){ //Agrupación
            sumaBloquesA += A[matchings[i].first].longitud;
        }
        else{
            Weight += sumaBloquesA/sumaBloquesB;
            //Set
            prevIndex_i = matchings[i].first;
            prevIndex_j = matchings[i].second;
            sumaBloquesA = A[matchings[i].first].longitud;
            sumaBloquesB = B[matchings[i].second].longitud;
        }
    }
    Weight += sumaBloquesA/sumaBloquesB;
    return Weight;
}

vector<Tupla> min_peso_bloques( int i, int j ){
    //cout<<"I: "<<i<< " J: "<<j<<endl;
    if( i == 0 ){
        vector<Tupla> retorno;
        for( int w = 0; w <= j-1 ; w++){
            retorno.emplace_back(Tupla(i,w));
        }
        return retorno;
    }
    else if( j == 0 ){
        vector<Tupla> retorno;
        for (int w = 0; w <= i-1; w++){
            retorno.emplace_back(Tupla(w,j));
        }
        return retorno;
    }
    else{
        vector<Tupla> ret1 = min_peso_bloques(i,j-1);
        ret1.emplace_back(i,j);

        vector<Tupla> ret2 = min_peso_bloques(i-1,j);
        ret2.emplace_back(i,j);

        double Weight_1 = GetWeight(ret1);
        double Weight_2 = GetWeight(ret2);

        return Weight_1 < Weight_2 ? ret1 : ret2 ;
    }
}

vector<Tupla> MIN_MATCHING(vector<int>& a, vector<int>& b){
    ObtenerBloques(A,a);
    ObtenerBloques(B,b);

    return min_peso_bloques( A.size()-1, B.size()-1) ;
}

int main(){
    //vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 0 , 1};
    //vector<int> b = { 0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1};
    vector<int> a = {0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1};
    vector<int> b = {0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0};
    vector<Tupla> temp = MIN_MATCHING(a,b);
    cout<<"MIN_MATCHING: "<< GetWeight(temp) << endl;
    for(auto& v : temp){
        cout<<"("<<v.first<<","<<v.second<<") ";
    }
    cout<<endl;
}
//(0,0) (1,0) (2,0) (3,1) (3,2) (4,3) (5,3)
