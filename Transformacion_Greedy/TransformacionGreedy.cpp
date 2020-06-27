#include "../Secuencias/Greedy/greedy.cpp"
#include "../Usefull2.cpp"




int main(){
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

        for(auto v : result.first){
            cout<<"("<<v.first<<","<<v.second<<") ";
        }
        cout << endl << result.second <<endl;
        sumatoria+=result.second;
    }
    cout<<"LA SUMTORIA ES: "<<sumatoria<<endl;


}
