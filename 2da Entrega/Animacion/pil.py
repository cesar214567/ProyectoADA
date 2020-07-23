from PIL import Image
from copy import copy
import os

width  = 800
height = 600

def LUM_601(imagen, GrayImg = False, filepath = None):
    if(GrayImg):
        GrayImage(imagen, 0.299, 0.587, 0.114, filepath)
    return convert(imagen, 0.299, 0.587, 0.114)

def LUM_709(imagen, GrayImg = False, filepath = None):
    if(GrayImg):
        GrayImage(imagen, 0.2126, 0.7152, 0.0722, filepath)
    return convert(imagen, 0.2126, 0.7152, 0.0722)

def LUM_240(imagen, GrayImg = False, filepath = None):
    if(GrayImg):
        GrayImage(imagen, 0.212, 0.701, 0.087, filepath)
    return convert(imagen, 0.212, 0.701, 0.087)

def LUM_input(imagen): 
    while(True):
        R = float(input("Ingrese el coeficiente de R: "))
        G = float(input("Ingrese el coeficiente de G: "))
        B = float(input("Ingrese el coeficiente de B: "))
        if(R+G+B == 1):
            op = input("¿Guardar la imagen?[y/n]: ")
            if(op.lower() == "y"):
                filepath = input("Ruta y nombre de la imagen: ")
                GrayImage(imagen, R, G, B, filepath)
            return convert(imagen,R,G,B)
        print("Los valores ingresados no son correctos. Ingrese nuevamente:")

def GrayImage(imagen, R, G, B, filepathD):
    try:
        os.remove(filepathD)
    except:
        pass
    image = Image.open(imagen)
    GrayImg = copy(image)
    width, height = image.size
    for y in range(height):
        for x in range(width):
            RGB = image.getpixel((x,y))
            Gris = int(RGB[0]*R + RGB[1]*G + RGB[2]*B)
            GrayImg.putpixel((x,y),(Gris,Gris,Gris))
    GrayImg.save(filepathD)

def SaveMatrix(matrix, filepath):
    try:
        os.remove(filepath)
    except:
        pass
    f = open(filepath, "w+")
    for i in range(len(matrix)):
        temporal=""
        for j in range(len(matrix[i])):
            temporal=temporal+str(matrix[i][j])+""
        temporal+="\n"
        f.write(temporal)
    f.close()

def convert(image, R, G, B):
    ConvertedMatrix01 = []

    for y in range(height):
        array01 = []
        for x in range(width):
        
            RGB = image.getpixel((x,y))
            Gris = int(RGB[0]*R + RGB[1]*G + RGB[2]*B)
            #Politica si el gris es 1 o 0 
            if(Gris > 122):
                array01.append(1)
            else:
                array01.append(0)
        ConvertedMatrix01.append(array01)
    return ConvertedMatrix01
        
def getImagenRGB(path):
    image = Image.open(path)
    image2 = image.resize((width,height))
    return image2 

def getRow(image,row): 
    retorno = []
    for y in range(width):
        retorno.append(image.getpixel((y,row)))
    return retorno

def ResultadoK(imagen,matrix):
    imagen = imagen.resize((width,len(matrix)))
    for y in range(len(matrix)):
        for x in range(width):
            imagen.putpixel((x,y),matrix[y][x])
    imagen.show()

def ArmarImagen(imagen,matrix,K,directorio): 
    try:
        os.makedirs(directorio)
    except:
        pass
    for y in range(height):
        for x in range(width):
            imagen.putpixel((x,y),matrix[K][y][x])
    
    imagen.save(directorio+"imagenIntermedia"+str(K+1)+".png")

if __name__ == "__main__":
    imgPath =  "../../Images/Abdullah.jpeg"
    
    #SaveMatrix(LUM_240(imgPath), "../../Text/matriz01.txt")
    SaveMatrix(LUM_input(imgPath), "../../Text/matriz01.txt")
    #testA = LUM_240(imgPath, GrayImg=True, filepath="../../Images/testA.png")
    #testB = LUM_709(imgPath, GrayImg=True, filepath="../../Images/testB.png")
    #testC = LUM_601(imgPath, GrayImg=True, filepath="../../Images/testC.png")
    #testD = LUM_input(imgPath)