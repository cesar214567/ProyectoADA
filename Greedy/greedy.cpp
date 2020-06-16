#include "../Useful.cpp"

vector<bloque> A;
vector<bloque> B;

double peso(vector<Tupla> &matchings){
    double suma_total=0;
    double tempa = A[matchings[0].first].longitud;
    double tempb = B[matchings[0].second].longitud;
    double t_a = matchings[0].first;
    double t_b = matchings[0].second;
    for (int i = 1 ; i < matchings.size(); i++){
        if(matchings[i].first == t_a){
            tempb += B[matchings[i].second].longitud;
        }
        else if (matchings[i].second == t_b){
            tempa += A[matchings[i].first].longitud;
        }
        else{
            suma_total += tempa/tempb;
            t_a = matchings[i].first;
            t_b = matchings[i].second;
            tempa = A[matchings[i].first].longitud;
            tempb = B[matchings[i].second].longitud;
        }
    }
    suma_total += tempa/tempb;
    return suma_total;
}

vector<Tupla> greedy_min() {
    int i, j;
    vector<Tupla> matchings;
    i = 0;
    j = 0;
    int cont_B = 0;
    int cont_A = 0;
    while (i < A.size() - 1 && j < B.size() - 1) {
        if (B[j + 1].longitud < B[j].longitud) {
            if (cont_B) {
                j++;
                i++;
                cont_B = 0;
            } else {
                matchings.emplace_back(Tupla(i, j));
                j++;
                cont_A++;
                if(j == B.size() - 1)
                    i++;
            }
        } else if (A[i].longitud < A[i + 1].longitud) {
            matchings.emplace_back(Tupla(i, j));
            if(cont_A){
                i++;
                j++;
                cont_B = 0;
                cont_A = 0;
            }else{
                i++;
                cont_B++;
                if(i == A.size()-1)
                    j++;
            }
        }
        else{
            matchings.emplace_back(Tupla(i, j));
            i++;
            j++;
            cont_B = 0;
            cont_A = 0;
        }
    }
    if (i == A.size() - 1) {
        while (j < B.size()) {
            matchings.emplace_back(Tupla(i, j));
            j++;
        }
    } else {
        while (i < A.size()) {
            matchings.emplace_back(Tupla(i, j));
            i++;
        }
    }
        return matchings;
    }
    
    
    pair<vector<Tupla>, double> MIN_MATCHING(vector<int> a, vector<int> b ) {
        ObtenerBloques(A,a);
        ObtenerBloques(B,b);
        pair<vector<Tupla>, double> ret1;
        ret1.first = greedy_min();
        ret1.second = peso(ret1.first);
        return ret1;
    }


int main() {
    vector<int> a; 
    vector<int> b; 
    Menu(a,b);
    auto result = MIN_MATCHING(a,b);

    for(auto v : result.first){
        cout<<"("<<v.first<<","<<v.second<<") ";
    }
    cout << endl << result.second <<endl;
    return 0;
}