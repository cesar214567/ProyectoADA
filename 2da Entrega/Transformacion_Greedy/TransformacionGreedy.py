#include "../Secuencias/Dinamica/dinamica.cpp"

import Useful


if __name__ == "__main__":
    auto temp= getMatriz();
    vector<vector<int>> matriz1;
    vector<vector<int>> matriz2;
    matriz1=temp.first;
    matriz2=temp.second;
    assert(matriz1.size()==matriz2.size());
    for (auto it:matriz1){
        for (auto it2:it){
            cout<<it2<<" "; 
        }
        cout<<endl;
    }
    cout<<endl;
    for (auto it:matriz2){
        for (auto it2:it){
            cout<<it2<<" "; 
        }
        cout<<endl; 
    }
    double sumatoria =0;
    for (int i=0;i<matriz1.size();i++){
        auto result = MIN_MATCHING(matriz1[i],matriz2[i]);
        GetTuplas( make_pair( matriz1[i].size()-1, matriz2[i].size()-1) );

        cout << "Tuplas: ";
        for (auto it : TuplasOPT){
        cout<<"("<<it.first<<","<<it.second<<") ";
        }
        cout << endl;
        sumatoria+=result;
    }
    cout<<"LA SUMTORIA ES: "<<sumatoria<<endl;


}
