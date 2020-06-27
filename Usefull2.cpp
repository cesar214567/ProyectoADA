#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <iomanip>
#include <utility>
#include <time.h>
#include <string.h>
#include <fstream>
#include <assert.h>
using namespace std;
 
pair<vector<vector<int>>,vector<vector<int>>> getMatriz(){
    vector<vector<int>> matriz1;
    vector<vector<int>> matriz2;
    string linea;
    fstream imput;

    imput.open("../imput.txt");
    while(getline(imput,linea)){
        vector<int> temp;
        if(linea=="B"){
            matriz2=matriz1;
            matriz1.clear();
            continue;
        }
        for (int i=0;i<linea.size();i++){
            temp.push_back(linea[i]-48);
        }
        matriz1.push_back(temp);
    }
    return make_pair(matriz2,matriz1);
}

/*int main(){
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
}
*/