import sys
sys.path.append("Algorithms/")
sys.path.append("Animacion/")
import Algorithms.TrGreedy as Tgd
import Algorithms.TrDynamic as Tdp
import Algorithms.TrImprovedDynamic as Tidp
import Animacion.animacion as ani
import Animacion.pil as pil
import Useful as us

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

def SelectNumImg():
    us.Num_IMG = int(input("Imagenes Intermedias: "))

def SelectLUM(img1, img2):
    txt = '''Seleccionar escala de grises:
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
        while(True):
            R = float(input("Ingrese el coeficiente de R: "))
            G = float(input("Ingrese el coeficiente de G: "))
            B = float(input("Ingrese el coeficiente de B: "))
            if(R+G+B == 1):
                matrixA = pil.convert(img1, R, G, B)
                matrixB = pil.convert(img2, R, G, B)
                break
            else:
                print("Los valores ingresados no son correctos, ingrese nuevamente.")
        return (matrixA, matrixB)
    else:
        sys.exit()

def Generar():
    SelectNumImg()
    #imgPath =  "../Images/Abdullah.jpeg"
    #imgPath2 = "../Images/Arnold_Schwarzenegger.jpg"
    imgPath =  "../Images/JoseMaria.jpeg"
    imgPath2 = "../Images/Ernesto.jpeg"
    
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
    txt = '''Seleccionar:
    1. Generar imagenes [1]
    2. Mostrar [2]
    3. Salir   [0]
    Opcion -> '''
    print(txt, end='')
    op = int(input(""))
    if(op == 1):
        Generar()
        Show()
    elif(op == 2):
        SelectNumImg()
        Show()
    else:
        sys.exit()

if __name__ == "__main__":
    main()