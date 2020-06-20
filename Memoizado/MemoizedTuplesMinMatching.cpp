#include "../Useful.cpp"
#include <map>
#include <ctime>


vector< vector<double> > Matrix;
map< pair<int,int>, pair<int,int> > minSubProblem; //Para GetTuplas_1

vector< int > sumaBloquesA;
vector< int > sumaBloquesB;

vector<bloque> A;
vector<bloque> B;
vector<Tupla> TuplasOPT;
vector<Tupla> TuplasOPT_1; //Para GetTuplas_1

double GetMatchDivision(int i, int m, int n){
	if(m == n) return double(A[i].longitud)/B[m].longitud;
	if(m == 0) return double(A[i].longitud)/sumaBloquesB[n];
	double suma = sumaBloquesB[n] - sumaBloquesB[m-1];
	
	return A[i].longitud/suma;
}

double GetMatchGroup(int r, int s, int j){
	if(r == s) return A[r].longitud/double(B[j].longitud);
	if(r == 0) return sumaBloquesA[s]/double(B[j].longitud);
	double suma = sumaBloquesA[s]-sumaBloquesA[r-1];
	
	return suma/B[j].longitud;
}

double Opt_Memoized(int i, int j){
	if(Matrix[i][j] != 0) {
		return Matrix[i][j];
	}else if ( i == 0 ){
	    Matrix[i][j] = GetMatchDivision(i,0,j);
    }else if ( j == 0 ){
	    Matrix[i][j] = GetMatchGroup(0,i,j);
	}else{
		double min_resultk = INT16_MAX;
        double min_resultl = INT16_MAX;

		int indexMinGroup, indexMinDivision; //extra

        for(int k = i; k >= 1; k--){
            auto Match = GetMatchGroup(k,i,j);
            auto SubProblem = Opt_Memoized(k-1,j-1);
            auto result  = SubProblem + Match;
			//Guardar el min peso
            if (min_resultk > result ) {
				min_resultk = result;
				indexMinGroup = k; //extra
			}
        }
		
        for(int l = j; l >= 1; l--){
            auto Match = GetMatchDivision(i,l,j);
            auto SubProblem =  Opt_Memoized(i-1,l-1);
            auto result = SubProblem + Match;
            //Guardar el min peso
            if (min_resultl > result) {
				min_resultl = result;
				indexMinDivision = l; //extra
			}
        }
		if(min_resultl > min_resultk){
			Matrix[i][j] = min_resultk;
			minSubProblem[make_pair(i,j)] = make_pair(indexMinGroup-1,j-1); //Usado en GetTuplas_1
		}else{
			Matrix[i][j] = min_resultl;
			minSubProblem[make_pair(i,j)] = make_pair(i-1,indexMinDivision-1); //Usado en GetTuplas_1
		}
	}
    return Matrix[i][j];
}
//No tan eficiente , /*** menos gasto de memoria ***/
void GetTuplas(int i, int j){

    if(i == 0){
        for(int aux_j = 0; aux_j <= j; aux_j++)
            TuplasOPT.emplace_back(i,aux_j);
        return;
    }else if(j == 0){
        for(int aux_i = 0; aux_i <= i; aux_i++)
            TuplasOPT.emplace_back(aux_i,j);
        return;
    }

    double min_resultk = INT16_MAX;
    double min_resultl = INT16_MAX;
    int indexMinGroup;
    int indexMinDivision;

    for(int k = i; k >= 1; k--){
        auto Match = GetMatchGroup(k,i,j);
        auto SubProblem = Matrix[k-1][j-1];
        auto result  = SubProblem + Match;
        //Guardar el min peso
        if (min_resultk > result ) {
            min_resultk = result;
            indexMinGroup = k;
        }
    }

    for(int l = j; l >= 1; l--){
        auto Match = GetMatchDivision(i,l,j);
        auto SubProblem =  Matrix[i-1][l-1];
        auto result = SubProblem + Match;
        //Guardar el min peso
        if (min_resultl > result) {
            min_resultl = result;
            indexMinDivision = l;
        }
    }
    if(min_resultl > min_resultk){
        GetTuplas(indexMinGroup-1,j-1);
        for(int aux_i = indexMinGroup; aux_i <= i; aux_i++)
            TuplasOPT.emplace_back(aux_i,j);

    }else{
        GetTuplas(i-1,indexMinDivision-1);
        for(int aux_j = indexMinDivision; aux_j <= j; aux_j++)
            TuplasOPT.emplace_back(i,aux_j);
    }

}
// /*** Eficiente ***/, gasta más memoria.
void GetTuplas_1(pair<int,int> OPT){
    pair<int,int> SubProblem = minSubProblem[OPT];

    if(SubProblem.first == 0){
        for(int j = 0; j <= SubProblem.second; j++)
            TuplasOPT_1.emplace_back(SubProblem.first, j);

    }else if(SubProblem.second == 0){
        for(int i = 0; i <= SubProblem.first; i++)
            TuplasOPT_1.emplace_back(i, SubProblem.second);

    }else GetTuplas_1(SubProblem);

    if(SubProblem.first + 1 == OPT.first){
        for(int j = SubProblem.second+1; j <= OPT.second; j++)
            TuplasOPT_1.emplace_back(OPT.first,j);
    }else{
        for(int i = SubProblem.first+1; i <= OPT.first; i++)
            TuplasOPT_1.emplace_back(i,OPT.second);
    }
}

double MIN_MATCHING(vector<int> a, vector<int> b){
	ObtenerBloques(A,a);
	ObtenerBloques(B,b);
	  
	sumaBloquesA.resize( A.size() ); sumaBloquesA[0] = A[0].longitud;
	for(int i = 1; i < A.size(); i++){
		sumaBloquesA[i] = A[i].longitud + sumaBloquesA[i-1];
	}
	sumaBloquesB.resize( B.size() ); sumaBloquesB[0] = B[0].longitud;
	for(int i = 1; i < B.size(); i++){
		sumaBloquesB[i] = B[i].longitud + sumaBloquesB[i-1];
	}

	Matrix.resize(A.size());  
	for(int i = 0; i < A.size(); i++) {
        Matrix[i].resize(B.size());
    }
	return Opt_Memoized( A.size()-1, B.size()-1 );
}


int main() {
    vector<int> a; //{0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1};
    vector<int> b; //{0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0};
    Menu(a,b);
    cout << "OPTIMO: " << MIN_MATCHING(a,b) << endl;

    cout<<"/****TIEMPO****/"<<endl;
    clock_t t0,t1;
    double time, time_1;

    t0 = clock();
	GetTuplas( A.size()-1, B.size()-1 );
    t1 = clock();
    time = (double(t1-t0)/CLOCKS_PER_SEC);

    cout << "Funcion Get_Tuplas, tiempo: "; cout << setprecision(10) << time;
    cout << endl;

    t0 = clock();
    GetTuplas_1( make_pair( A.size()-1, B.size()-1) );
    t1 = clock();
    time_1 = (double(t1-t0)/CLOCKS_PER_SEC);

    cout << "Funcion Get_Tuplas_1, tiempo: "; cout << setprecision(10) << time_1;
    cout << endl;

    /*
    cout << "Tuplas: ";
    for (auto it : TuplasOPT){
      cout<<"("<<it.first<<","<<it.second<<") ";
    }
    cout << endl;*/
}