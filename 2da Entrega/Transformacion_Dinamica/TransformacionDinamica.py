import sys 
sys.path.append("../Dinamica")
import dinamica as dp
import Useful as us

MatrixBloquesA = []
MatrixBloquesB = []
MatrixMatchings = []

def TransformacionDinamica(matrixA, matrixB):
    assert len(matrixA) == len(matrixB), "Incompatibles"
    global MatrixMatchings, MatrixBloquesA, MatrixBloquesB
    sumatoria = 0.0
    for i in range(0, len(matrixA)):
        result = dp.MIN_MATCHING(matrixA[i], matrixB[i])
        dp.GetTuplas( (len(dp.A)-1, len(dp.B)-1) )
        
        MatrixMatchings.append(list(dp.TuplasOPT))
        MatrixBloquesA.append(list(dp.A))
        MatrixBloquesB.append(list(dp.B))
        
        sumatoria = sumatoria + result
    return (sumatoria)

if __name__ == "__main__":
    matriz1 = us.GetMatriz("../../Text/inputA.txt")
    matriz2 = us.GetMatriz("../../Text/inputB.txt")
    us.ImprimirMatriz(matriz1)
    us.ImprimirMatriz(matriz2)
    result = TransformacionDinamica(matriz1, matriz2)
    print("Resultado: ", result)
    for match in MatrixMatchings:
        print(match)