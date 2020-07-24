
import sys
sys.path.append("../../")
import Useful as us
sys.path.append("../")
import TrDynamic as Dyn
import TrGreedy as Greed
import TrImprovedDynamic as impr


if __name__ == "__main__":
    matriz1 = us.GetMatriz("../../../Text/inputA.txt")
    matriz2 = us.GetMatriz("../../../Text/inputB.txt")
    us.ImprimirMatriz(matriz1)
    us.ImprimirMatriz(matriz2)
    #result = Dyn.TrDynamic(matriz1, matriz2)
    #result = Greed.TrGreedy(matriz1,matriz2)
    result = impr.TrImprovedDynamic(matriz1,matriz2)
    print("Resultado: ", result)
    for match in impr.MatrixMatchings:
        print(match)