#include "../Useful.cpp"

vector<bloque> A;
vector<bloque> B;

pair<vector<Tupla>, double> GetMatchDivision(int i, int m, int n){
	vector<Tupla> matchs;
	double suma = 0.0;
	for(int p = m; p <= n; p++){
		matchs.emplace_back(i,p);
		suma += B[p].longitud;
	}
	return make_pair(matchs, A[i].longitud/suma);
}

pair<vector<Tupla>, double> GetMatchGroup(int r, int s, int j){
	vector<Tupla> matchs;
	double suma = 0.0;
	for(int p = r; p <= s; p++){
		matchs.emplace_back(p,j);
		suma += A[p].longitud;
	}
	return make_pair(matchs, suma/B[j].longitud);
}

pair<vector<Tupla>, double> min_peso_bloques(int i, int j){
    if ( i == 0 ){
        return GetMatchDivision(i,0,j);
    }else if ( j == 0 ){
        return GetMatchGroup(0,i,j);
    }else{
        double min_resultk = INT16_MAX;
        double min_resultl = INT16_MAX;

        pair<vector<Tupla>,double> Matchk;
        pair<vector<Tupla>,double> SubProblemk;

        pair<vector<Tupla>,double> Matchl;
        pair<vector<Tupla>,double> SubProbleml;

        vector<Tupla> matchsk;
        vector<Tupla> matchsl;

        for(int k = i; k >= 1; k--){
            auto Match = GetMatchGroup(k,i,j);
            auto SubProblem = min_peso_bloques(k-1,j-1);
            auto result  = SubProblem.second + Match.second;
			
            if (min_resultk > result ) {
                min_resultk = result; //Guardar el min peso
                Matchk = Match; SubProblemk = SubProblem; //Tuplas
            }
        }
		
        matchsk.insert( matchsk.begin(), begin(SubProblemk.first), end(SubProblemk.first) );
        matchsk.insert( matchsk.end(), begin(Matchk.first), end(Matchk.first) );

        for(int l = j; l >= 1; l--){
            auto Match = GetMatchDivision(i,l,j);
            auto SubProblem =  min_peso_bloques(i-1,l-1);
            auto result = SubProblem.second + Match.second;
            
            if (min_resultl > result) {
                min_resultl = result; //Guardar el min peso
                Matchl = Match; SubProbleml = SubProblem; //Guardar las Tuplas
            }
        }

        matchsl.insert( matchsl.begin(), begin(SubProbleml.first), end(SubProbleml.first) );
        matchsl.insert( matchsl.end(), begin(Matchl.first), end(Matchl.first) );

        if( min_resultk > min_resultl ) return make_pair( matchsl , min_resultl );
        else return make_pair( matchsk , min_resultk );
    }
}

pair<vector<Tupla>, double> MIN_MATCHING(vector<int> a, vector<int> b){
  ObtenerBloques(A,a);
  ObtenerBloques(B,b);
  
  return min_peso_bloques( A.size()-1, B.size()-1 ) ;
}

int main() {
    vector<int>a;
    vector<int>b;
    Menu(a,b);
    auto result = MIN_MATCHING(a,b);

    cout << "Optimo: " << result.second << endl;
    for(auto v : result.first){
        cout<<"("<<v.first<<","<<v.second<<") ";
    }
    cout<<endl;
  
}
