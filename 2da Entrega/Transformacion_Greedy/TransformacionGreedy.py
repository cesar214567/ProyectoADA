import sys 
sys.path.append("../")
sys.path.append("../Greedy/")
import Greedy as greed
import Useful as us

if __name__ == "__main__":
    mat1 = us.getMatriz("matriz01.txt")
    mat2 = us.getMatriz("matriz02.txt")
    matriz1 = []
    matriz2 = []
    assert(mat1.size() == mat2.size())

    for  it in matriz1:
        for it2  in it:
            print(it2, end = " ") 
        print("") 
    print("")
    
    for it in matriz2:
        for it2 in it:
            print(it2, end = " ") 
        print("") 


    sumatoria =0

    for i in range(0,len(matriz1)):
        result = greed.MIN_MATCHING(matriz1[i],matriz2[i])

        for v in result[0]:
            print("(" + str(v[0] + "," + v[1] + ") " , end = ""))
        print ( "\n " + str(result[1]))
        sumatoria += result[1]
    
    print("LA SUMTORIA ES: " + str(sumatoria))
    

