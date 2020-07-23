import sys
sys.path.append("Algorithms/")
sys.path.append("Animacion/")
import Algorithms.TrGreedy as Tgd
import Algorithms.TrDynamic as Tdp
import Algorithms.TrImprovedDynamic as Tidp
import Animacion.animacion as ani
import Animacion.pil as pil

GreedyDirectory = "../Images/GreedyImages/"
DynamicDirectory = "../Images/DpImages/"
ImprovedDynamicDirectory = "../Images/IDpImages/"

def SelectAlgorithm(img1, img2, matrixA, matrixB):
    txt = '''Seleccionar Algoritmo:
    1. Greedy   [1]
    2. Dinamica [2]
    3. Dinamica Mejorada [3]
    4. Salir [0]
    Opcion -> '''
    print(txt, end='')
    op = int(input())
    if(op == 1):
        Tgd.TrGreedy(matrixA, matrixB, True)
        ani.GenerarImagenesIntermedias(img1, img2, \
                        Tgd.MatrixMatchings, GreedyDirectory)
    elif(op == 2):
        Tdp.TrDynamic(matrixA, matrixB, True)
        ani.GenerarImagenesIntermedias(img1, img2, \
                        Tdp.MatrixMatchings, DynamicDirectory)
    elif(op == 3):
        Tidp.TrImprovedDynamic(matrixA, matrixB, True)
        ani.GenerarImagenesIntermedias(img1, img2, \
                        Tidp.MatrixMatchings, ImprovedDynamicDirectory)
    else:
        sys.exit()

def SelectLUM(img1, img2):
    txt = '''Seleccionar Algoritmo:
    1. LUM_601   [1]
    2. LUM_709   [2]
    3. LUM_240   [3]
    4. LUM_input [4]
    5. Salir     [0]
    Opcion -> '''
    print(txt, end='')
    op = int(input(""))
    if(op == 1):
        matrixA = pil.LUM_601(img1)
        matrixB = pil.LUM_601(img2)
        return (matrixA, matrixB)
    elif(op == 2):
        matrixA = pil.LUM_709(img1)
        matrixB = pil.LUM_709(img2)
        return (matrixA, matrixB)
    elif(op == 3):
        matrixA = pil.LUM_240(img1)
        matrixB = pil.LUM_240(img2)
        return (matrixA, matrixB)
    elif(op == 4):
        matrixA = pil.LUM_input(img1)
        matrixB = pil.LUM_input(img2)
        return (matrixA, matrixB)
    else:
        sys.exit()

def Generar():
    imgPath =  "../Images/Abdullah.jpeg"
    imgPath2 = "../Images/Arnold_Schwarzenegger.jpg"
    img1 = pil.getImagenRGB(imgPath)
    img2 = pil.getImagenRGB(imgPath2)
    matriz01, matriz02 = SelectLUM(img1, img2)
    SelectAlgorithm(img1, img2, matriz01, matriz02)

def Show():
    txt = '''Mostrar :
    1. Greedy     [1]
    2. Dinamica   [2]
    3. Dinamica Mejorada [3]
    4. Salir      [0]
    Opcion -> '''
    print(txt, end='')
    op = int(input(""))
    if(op == 1):
        ani.MostrarAnimacion(GreedyDirectory)
    elif(op == 2):
        ani.MostrarAnimacion(DynamicDirectory)
    elif(op == 3):
        ani.MostrarAnimacion(ImprovedDynamicDirectory)
    else:
        sys.exit()

def main():
    Generar()
    Show()

if __name__ == "__main__":
    main()