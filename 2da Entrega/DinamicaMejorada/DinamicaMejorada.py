import math
import sys
sys.path.append("../")
import Useful as us

Matrix = []
minSubProblem = {}  # Para GetTuplas_1

sumaBloquesA = []
sumaBloquesB = []

A = []
B = []
TuplasOPT = []

u = 0.0

def GetMatchDivision(i, m, n):
    if(m == n):
        return abs(float(A[i].longitud)/B[m].longitud - u)
    if(m == 0):
        return abs(float(A[i].longitud)/sumaBloquesB[n] - u)

    suma = sumaBloquesB[n] - sumaBloquesB[m-1]
    return abs(float(A[i].longitud)/suma - u)


def GetMatchGroup(r, s, j):
    if(r == s):
        return abs(A[r].longitud/float(B[j].longitud) - u)
    if(r == 0):
        return abs(sumaBloquesA[s]/float(B[j].longitud) - u)
    suma = sumaBloquesA[s] - sumaBloquesA[r-1]

    return abs(suma/float(B[j].longitud) - u)


def OPT_Result(i, j):
    global Matrix
    if(i == 0):
        Matrix[i][j] = GetMatchDivision(i, 0, j)
    elif(j == 0):
        Matrix[i][j] = GetMatchGroup(0, i, j)
    else:
        min_resultk = math.inf
        min_resultl = math.inf

        indexMinGroup = 0
        indexMinDivision = 0  # extra

        for k in range(i, 0, -1):
            Match = GetMatchGroup(k, i, j)
            SubProblem = Matrix[k-1][j-1]
            result = SubProblem + Match
            # Guardar el min peso
            if(min_resultk > result):
                min_resultk = result
                indexMinGroup = k

        for l in range(j, 0, -1):
            Match = GetMatchDivision(i, l, j)
            SubProblem = Matrix[i-1][l-1]
            result = SubProblem + Match
            # Guardar el min peso
            if(min_resultl > result):
                min_resultl = result
                indexMinDivision = l

        if(min_resultl > min_resultk):
            Matrix[i][j] = min_resultk
            minSubProblem[i, j] = (indexMinGroup-1, j-1)
        else:
            Matrix[i][j] = min_resultl
            minSubProblem[i, j] = (i-1, indexMinDivision-1)


def DynamicProgramming(x, y):
    for i in range(0, x):
        for j in range(0, y):
            OPT_Result(i, j)

    OPT_Result(x, y)

    return Matrix[x][y]


def GetTuplas(OPT):
    if(OPT[0] == 0):
        for j in range(0, OPT[1]+1):
            TuplasOPT.append([OPT[0], j])
    elif(OPT[1] == 0):
        for i in range(0, OPT[0]+1):
            TuplasOPT.append([i, OPT[1]])
    else:
        SubProblem = minSubProblem[OPT]
        GetTuplas(SubProblem)
        if(SubProblem[0] + 1 == OPT[0]):
            for j in range(SubProblem[1]+1, OPT[1]+1):
                TuplasOPT.append([OPT[0], j])
        else:
            for i in range(SubProblem[0]+1, OPT[0]+1):
                TuplasOPT.append([i, OPT[1]])

def InicializarSumaBloques():
    global sumaBloquesA
    global sumaBloquesB

    sumaBloquesA.clear()
    sumaBloquesA.append(A[0].longitud)
    for i in range(1, len(A)):
        sumaBloquesA.append(A[i].longitud + sumaBloquesA[i-1])

    sumaBloquesB.clear()
    sumaBloquesB.append(B[0].longitud)
    for i in range(1, len(B)):
        sumaBloquesB.append(B[i].longitud + sumaBloquesB[i-1])


def InicializarMatrix():
    global Matrix
    Matrix.clear()
    for i in range(0, len(A)):
        Matrix.append([])
    for i in range(0, len(A)):
        Matrix[i] = [0]*len(B)

def InicializarU():
    global u
    u = float(sumaBloquesA[len(A)-1])/float(sumaBloquesB[len(B)-1])

def Inicializar():
    TuplasOPT.clear()
    minSubProblem.clear()
    InicializarSumaBloques()
    InicializarU()
    InicializarMatrix()

def MIN_MATCHING(a, b):
    global A
    global B

    A = us.ObtenerBloques(a)
    B = us.ObtenerBloques(b)
    if(len(A) == 0 or len(B) == 0):
        return 0
    else:
        Inicializar()
        result = DynamicProgramming(len(A)-1, len(B)-1)
        GetTuplas((len(A)-1, len(B)-1))
        return result


if __name__ == "__main__":
    # a = [0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1]
    # b = [0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0]
    # a = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
    # b = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    a = []
    b = []
    us.Menu(a, b)
    print("OPTIMO: " + str(MIN_MATCHING(a, b)) + "\n")
    print(u)
    print("Tuplas: ")
    for it in TuplasOPT:
        print("(" + str(it[0]) + "," + str(it[1]) + ")", end=' ')
    print("")