from PIL import Image
import os

def LUM_601(imagen):
    convert(imagen,0.299,0.587,0.114)

def LUM_709(imagen):
    convert(imagen,0.2126,0.7152,0.0722)

def LUM_240(imagen):
    convert(imagen, 0.212, 0.701, 0.087)

def LUM_input(imagen): 
    while(True):
        R = float(input("Ingrese el coeficiente de R: "))
        G = float(input("Ingrese el coeficiente de G: "))
        B = float(input("Ingrese el coeficiente de B: "))
        if( R+G+B == 1):
            convert(imagen,R,G,B)
            break
        print("Los valores ingresados no son correctos. Ingrese nuevamente:")
     

def convert(imagen,R,G,B):
    os.remove("matriz01.txt")
    os.remove("matrizL.txt")
   #image = Image.open("Abdullah.jpeg")
    image = Image.open(imagen)
    xsize,ysize=image.size

    file = open("matrizL.txt","w+")
    file2= open("matriz01.txt","w+")
    
    matriz0=[]
    matrizL=[]
    
   # imgGris = image

    for x in range(xsize):
        arr0=[]
        arrL=[]
        for y in range(ysize):
            RGB = image.getpixel((x,y))
            Gris = int(RGB[0]*R + RGB[1]*G + RGB[2]*B)
            #imgGris.putpixel((x,y),(Gris,Gris,Gris))
            arrL.append(Gris)
            #Politica si el gris es 1 o 0 
            if(Gris > 122):
                arr0.append(1)
            else:
                arr0.append(0)
        matrizL.append(arrL)
        matriz0.append(arr0)
    
    #imgGris.show()

    for x in range(xsize):
        temporal=""
        for y in range(ysize):
            temporal=temporal+str(matrizL[x][y])+" "
        temporal+="\n"
        file.write(temporal)

    for x in range(xsize):
        temporal=""
        for y in range(ysize):
            temporal=temporal+str(matriz0[x][y])+" "
        temporal+="\n"
        file2.write(temporal)
        

if __name__ == "__main__":

    
    imgPath =  "Abdullah.jpeg"
    LUM_240(imgPath)
    LUM_601(imgPath)
    LUM_709(imgPath)      
    

