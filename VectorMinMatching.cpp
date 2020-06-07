#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <utility>
#define p 9 
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

//A = [ 0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 1]
//B = [ 0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1]

vector<bloque> A;
vector<bloque> B;

pair<vector<Tupla>, double> min_peso_bloques(int r , int s, int i, int j){
    if ( r == s ){
        vector<Tupla> matchs;
        double suma = 0.0;

        for(int m = i; m <= j; m++) {
            matchs.emplace_back( r, m );
            suma += B[m].longitud;
        }
        return make_pair ( matchs , A[r].longitud/suma );

    }else if ( i == j ){
        vector<Tupla> matchs;
        double suma = 0.0;

        for(int m = r; m <= s; m++) {
            matchs.emplace_back( m, i );
            suma += A[m].longitud;
        }
        return make_pair ( matchs , suma/B[i].longitud );
    } else{
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

        if( min_resultk > min_resultl ) return make_pair( matchsl , min_resultl );
        else return make_pair( matchsk , min_resultk );

    }
}
pair<vector<Tupla>, double> MIN_MATCHING(int a[], int b[]){
  //A={0 1 1 1 0 0 1 1 }
  int cont= 0; 
  bool c = false; 
  for(int i = 0; i < p ; i++){
    if(a[i]){
      cont++;
      c = true;
      if(i == p-1){
        A.emplace_back(bloque(i-cont+1,i,cont));  
      }
    }
    else if(cont){
      A.emplace_back(bloque(i-cont,i-1,cont));
      cont = 0;
      c = false;
    } 
    
  }
  cont= 0; 
  c = false; 
  for(int i = 0; i < p ; i++){
    if(b[i]){
      cont++;
      c = true;
      if(i == p-1){
        B.emplace_back(bloque(i-cont+1,i,cont));  
      }
    }
    else if(cont){
      B.emplace_back(bloque(i-cont,i-1,cont));
      cont = 0;
      c = false;
    }   
  }
  return min_peso_bloques(0,A.size()-1, 0,B.size()-1) ;
}

int main() {
  
    int a[p]={0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0};
    int b[p]={0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1};
    
    auto result = MIN_MATCHING(a,b);

    cout << "Optimo: " << result.second << endl;
    for(auto v : result.first){
        cout<<"("<<v.first<<","<<v.second<<") ";
    }
  
    
}
