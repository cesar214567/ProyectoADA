import sys 
import Dynamic as dp

sys.path.append("../")
import Useful as us

MatrixMatchings = []

def TrDynamic(matrixA, matrixB, GetSubmatching = False):
    global MatrixMatchings
    if(GetSubmatching):
        for i in range(0, len(matrixA)):
            result = dp.MIN_MATCHING(matrixA[i], matrixB[i], GetSubmatching)
            MatrixMatchings.append(list(result))
    else:
        sumatoria = 0.0
        for i in range(0, len(matrixA)):
            result = dp.MIN_MATCHING(matrixA[i], matrixB[i])
            sumatoria = sumatoria + result
            MatrixMatchings.append(list(dp.TuplasOPT))
        return sumatoria