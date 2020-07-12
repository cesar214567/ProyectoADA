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
 
vector<vector<int>> getMatriz(string txt){
    vector<vector<int>> matriz1;
    string linea;
    fstream imput;

    imput.open(txt);
    while(getline(imput,linea)){
        vector<int> temp;
        for (int i=0;i<linea.size();i++){
            temp.push_back(linea[i]-48);
        }
        matriz1.push_back(temp);
    }
    return matriz1;
}

