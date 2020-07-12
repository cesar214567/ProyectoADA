import sys 
sys.path.append("../Dinamica")
import dinamica us dp

def ImprimirMatriz(matrix):
    for it in matrix:
        for it2 in it:
            print(str(it2), end=' ')
        print("\n")
    print("\n")

if __name__ == "__main__":
    temp = us.GetMatriz()
    matriz1 = temp[0]
    matriz2 = temp[1]
    assert(len(matriz1) == len(matriz2), "Incompatibles")

    ImprimirMatriz(matriz1)
    ImprimirMatriz(matriz2)

    sumatoria = 0.0

    for i in range(0, len(matriz1)):
        result = dp.MIN_MATCHING(matriz1[i], matriz2[i])
        dp.GetTuplas( (len(matriz1)-1, len(matriz2)-1) )
        for tupla in dp.TuplasOPT:
            print("("+str(tupla[0])+","+str(tupla[1])+")", end=' ')
        print("\n")
        sumatoria = sumatoria + result
    print("La sumatoria es: "+str(sumatoria))    