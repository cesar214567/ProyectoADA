import sys 
sys.path.append("../DinamicaMejorada")
import DinamicaMejorada as idp
import Useful as us

MatrixBloquesA = []
MatrixBloquesB = []
MatrixMatchings = []

def TransformacionDinamicaMejorada(matrixA, matrixB):
    assert len(matrixA) == len(matrixB), "Incompatibles"
    global MatrixMatchings, MatrixBloquesA, MatrixBloquesB
    sumatoria = 0.0
    for i in range(0, len(matrixA)):
        result = idp.MIN_MATCHING(matrixA[i], matrixB[i])
        print(idp.u)
        MatrixMatchings.append(list(idp.TuplasOPT))
        MatrixBloquesA.append(list(idp.A))
        MatrixBloquesB.append(list(idp.B))
        
        sumatoria = sumatoria + result
    return (sumatoria)

if __name__ == "__main__":
    matriz1 = us.GetMatriz("../../Text/inputA.txt")
    matriz2 = us.GetMatriz("../../Text/inputB.txt")
    us.ImprimirMatriz(matriz1)
    us.ImprimirMatriz(matriz2)
    result = TransformacionDinamicaMejorada(matriz1, matriz2)
    print("Resultado: ", result)
    for match in MatrixMatchings:
        print(match)