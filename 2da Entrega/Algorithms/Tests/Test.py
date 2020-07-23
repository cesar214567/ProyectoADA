import sys
sys.path.append("../")
sys.path.append("../../")
import Dynamic as dp
import Greedy as gd
import ImprovedDynamic as idp 
import Useful as us

a = []
b = []
result = 0

def SpecificTest():
    global a, b
    #a = [0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1]
    #b = [0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0]
    #a = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
    #b = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    a = [1, 0, 1, 1, 0, 1, 0]
    b = [1, 1, 0, 1, 1, 0, 1]

def PrintTuplas(Tuplas):
    for it in Tuplas:
        print("(" + str(it[0]) + "," + str(it[1]) + ")", end=' ')
    print("")

def PrintSubMatching(submatchings):
    for it in submatchings:
        it.printear()

def GreedyAlgorithm():
    result = gd.MIN_MATCHING(a, b)
    print("Resultado[Greedy]: "+str(result))
    PrintTuplas(gd.matchings)
    sub = int(input("Imprimir Submatching[Si(1)/No(0)]: "))
    if(sub == 1):
        PrintSubMatching(us.GetSubMatchings(gd.matchings, gd.A, gd.B))

def DynamicAlgorithm():
    result = dp.MIN_MATCHING(a, b)
    print("Resultado[Dinamica]: "+str(result))
    PrintTuplas(dp.TuplasOPT)
    sub = int(input("Imprimir Submatching[Si(1)/No(0)]: "))
    if(sub == 1):
        PrintSubMatching(us.GetSubMatchings(dp.TuplasOPT, dp.A, dp.B))

def ImprovedDynamicaAlgorithm():
    result = idp.MIN_MATCHING(a, b)
    print("Constante u: "+str(idp.u))
    print("Resultado[DinamicaMejorada]: "+str(result))
    PrintTuplas(idp.TuplasOPT)
    sub = int(input("Imprimir Submatching[Si(1)/No(0)]: "))
    if(sub == 1):
        PrintSubMatching(us.GetSubMatchings(idp.TuplasOPT, idp.A, idp.B))

def SelectAlgorithm():
    txt = '''Seleccionar Algoritmo:
    1. Greedy   [1]
    2. Dinamica [2]
    3. Dinamica Mejorada [3]
    4. Salir [0]
    Opcion -> '''
    print(txt, end='')
    op = int(input())
    if(op == 1):
        GreedyAlgorithm()    
    elif(op == 2):
        DynamicAlgorithm()
    elif(op == 3):
        ImprovedDynamicaAlgorithm()
    else:
        sys.exit()

def main():
    global a, b
    us.Menu(a, b)
    #SpecificTest()
    SelectAlgorithm()

if __name__ == "__main__":
    main()