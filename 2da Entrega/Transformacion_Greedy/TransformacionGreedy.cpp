#include "../Secuencias/Greedy/greedy.cpp"
#include "../Usefull2.cpp"

int main(){
    auto mat1= getMatriz("matriz01.txt");
    auto mat2= getMatriz("matriz02.txt");
    vector <vector<int>> matriz1;
    vector <vector<int>> matriz2;
    assert(mat1.size() == mat2.size());

    for (auto it:matriz1){
        for (auto it2 : it){
            cout << it2 <<" "; 
        }
        cout << endl;
    }
    cout << endl;
    
    for (auto it:matriz2){
        for (auto it2:it){
            cout << it2 << " "; 
        }
        cout << endl; 
    }

    double sumatoria =0;
    for (int i = 0; i < matriz1.size(); i++){
        auto result = MIN_MATCHING(matriz1[i],matriz2[i]);
        
        for(auto v : result.first){
            cout << "(" << v.first << "," << v.second <<") ";
        }
        cout << endl << result.second <<endl;
        sumatoria += result.second;
    }
    cout << "LA SUMTORIA ES: " << sumatoria << endl;

}
