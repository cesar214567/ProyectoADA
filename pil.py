from PIL import Image
import os


os.remove("matriz01.txt")
os.remove("matrizL.txt")
image = Image.open("Abdullah.jpeg")
xsize,ysize=image.size
for x in range(10):
    for y in range(10):
        arr=[x,y]
        tupla=tuple(arr)
image = image.convert("L")
image.show()
file = open("matrizL.txt","w+")
file2= open("matriz01.txt","w+")
matriz0=[]
matrizL=[]
for x in range(xsize):
    arr0=[]
    arrL=[]
    for y in range(ysize):
        arr=[x,y]
        tupla=tuple(arr)
        arrL.append(image.getpixel(tupla))
        if(image.getpixel(tupla)>122):
            arr0.append(1)
        else:
            arr0.append(0)
    matrizL.append(arrL)
    matriz0.append(arr0)

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
    

