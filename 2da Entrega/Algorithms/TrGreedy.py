import sys 
import Greedy as gd

sys.path.append("../")
import Useful as us

MatrixMatchings = []

def TrGreedy(matrixA, matrixB, GetSubmatching = False):
    global MatrixMatchings
    if(GetSubmatching):
        for i in range(0, len(matrixA)):
            result = gd.MIN_MATCHING(matrixA[i], matrixB[i], GetSubmatching)
            MatrixMatchings.append(list(result))
    else:
        sumatoria = 0.0
        for i in range(0, len(matrixA)):
            result = gd.MIN_MATCHING(matrixA[i], matrixB[i])
            sumatoria = sumatoria + result
            MatrixMatchings.append(list(gd.matchings))
        return sumatoria