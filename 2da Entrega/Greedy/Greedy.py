
#include "../Useful.cpp"
import sys
sys.path.append("../")
import Useful as us
sys.path.append("../Procesamiento")
import pil2 as pil
from math import ceil,floor
import numpy as np

A = []
B = []

def peso(matchings):
    global A
    global B
    suma_total=0
    if len(matchings)==0:
        return 0
    t_a = matchings[0][0]
    t_b = matchings[0][1]
    tempa = A[t_a].longitud
    tempb = B[t_b].longitud
    for i in range  (1,len(matchings),1):
        if(matchings[i][0] == t_a):
            tempb += B[matchings[i][1]].longitud
        
        elif (matchings[i][1] == t_b):
            tempa += A[matchings[i][0]].longitud
        else:
            suma_total += tempa/tempb
            t_a = matchings[i][0]
            t_b = matchings[i][1]
            tempa = A[matchings[i][0]].longitud
            tempb = B[matchings[i][1]].longitud
    suma_total += tempa/tempb
    return suma_total


def greedy_min():
    matchings = []
    i = 0
    j = 0
    cont_B = 0
    cont_A = 0
    while (i < len(A) - 1 and j < len(B) - 1):
        if (B[j + 1].longitud < B[j].longitud):
            if (cont_B):
                j += 1
                i += 1
                cont_B = 0
            else:
                matchings.append([i,j])
                j += 1
                cont_A += 1
                if( j == len(B)- 1 ):
                    i += 1  
        elif (A[i].longitud < A[i + 1].longitud):
            matchings.append([i,j])
            if(cont_A):
                i += 1
                j += 1 
                cont_B = 0
                cont_A = 0
            else:
                i += 1
                cont_B += 1 
                if(i == len(A)-1):
                    j += 1
        else:
            matchings.append([i,j])
            i += 1 
            j += 1 
            cont_B = 0
            cont_A = 0

    if (i == len(A) - 1):
        while (j < len(B)):
            matchings.append([i,j])
            j += 1
    else:
        while (i < len(A)):
            matchings.append([i,j])
            i += 1

    return matchings
    
        
def MIN_MATCHING(a, b):
    global A
    global B
    A = us.ObtenerBloques(a)
    B = us.ObtenerBloques(b)
    
    ret1 = greedy_min()
    
    ret2 = peso(ret1)
    ret3 = us.GetSubMatchings(ret1,A,B)
    ret = (ret1, ret2, ret3)
    return ret


if __name__ == "__main__":
    
    imgPath =  "../../Images/Abdullah.jpeg"
    imgPath2 = "../../Images/Arnold_Schwarzenegger.jpg"
    img1 =pil.getImagenRGB(imgPath)
    img2 =pil.getImagenRGB(imgPath2)
    matriz01 = pil.convert(img1,0.2,0.6,0.2)
    matriz02 = pil.convert(img2,0.2,0.6,0.2)
    for i in matriz01:
        for j in i:
            print(j,end=" ")
        print("")

    print("")
    print("")
    print("")
    print("")
    print("")

    print("")
    print("")
    print("")
    print("")
    print("")

    print("")
    print("")
    print("")
    print("")
    print("")
    for i in matriz02:
        for j in i:
            print(j,end=" ")
        print("")    
    row11 = pil.getRow(img1,0)
    row12 = pil.getRow(img2,0)
    
    #a = []; 
    a = matriz01[0]
    #b = []; 
    b = matriz02[0]
    #us.Menu(a,b)
    result = MIN_MATCHING(a,b)
    matchings=result[2]
    antimatchings=us.GetAntiMatching(matchings)

    
    for v in result[0]: 
        print("(" + str(v[0])  + "," + str(v[1]) + ") ",end = " ")

    print("\n " + str(result[1]))
    
    for submatching in matchings: 
        submatching.getProporcionalidad()
        submatching.printear2()
    print("-------------------------------------------------------wtf")
    #matchings[len(matchings)-1].printear3()

    for submatching in antimatchings:
        submatching.getProporcionalidad()
        submatching.printear2()
    print("-----------------------------------------")
    matrix=[]
    matrix.append(row11)

    # Sacamos el diferencial entre un pixel de la imagen b y uno de la imagen a entre i iteraciones 
    for i in range(us.Num_IMG-1):
        lista= []
        for j in range(len(row11)):
            init=[]
            R = row11[j][0]+ (float(i+1)/float(us.Num_IMG))* (row12[j][0]-row11[j][0])
            G = row11[j][1]+ (float(i+1)/float(us.Num_IMG))* (row12[j][1]-row11[j][1])
            B = row11[j][2]+ (float(i+1)/float(us.Num_IMG))* (row12[j][2]-row11[j][2])
            init.append((R,G,B))
            lista.append(init)
        matrix.append(lista)
    
    # Agregamos los demas pixeles a la lista 
    
    for j in range(len(matchings)):
        proporcionalidades=matchings[j].proporcionalidad
        if (matchings[j].isDivision()): 
            for index in range(len(proporcionalidades)):
                inicio1= proporcionalidades[index][0]
                end1 = proporcionalidades[index][1]
                inicio2 =float(matchings[j].subB[index].start)
                end2 =float(matchings[j].subB[index].end)
                tamano_total=ceil(end1)-floor(inicio1)
                #hacer el calculo para cada iteracion
                for k in range(us.Num_IMG-1):
                    initK = inicio1 + (k+1)*(inicio2-inicio1)/float(us.Num_IMG)
                    endK = end1 + (k+1)*(end2-end1)/float(us.Num_IMG)
                    long_pixel_K = (endK-initK)/float(tamano_total)
                    for t in np.arange(initK,endK,long_pixel_K):
                        rango = long_pixel_K/float(matchings[j].subB[index].longitud)
                        cont = floor(inicio2)
                        cont2 = t
                        for pixel in range(floor(t),ceil(t+long_pixel_K),1):
                            if pixel > cont2 + rango: 
                                cont = cont + 1
                                cont2 = cont2 + rango
                            print(initK)
                            print(cont)
                            R = int(row11[floor(t)][0] + (float(k+1)/float(us.Num_IMG))* (row12[cont][0]-row11[floor(t)][0]))
                            G = int(row11[floor(t)][1] + (float(k+1)/float(us.Num_IMG))* (row12[cont][1]-row11[floor(t)][1]))
                            B = int(row11[floor(t)][2] + (float(k+1)/float(us.Num_IMG))* (row12[cont][2]-row11[floor(t)][2]))
                            matrix[k+1][pixel].append((R,G,B))
        else:
            for index in range(len(proporcionalidades)):
                inicio1 = float(matchings[j].subA[index].start)
                end1 = float(matchings[j].subA[index].end)
                inicio2 = proporcionalidades[index][0]
                end2 = proporcionalidades[index][1]
                tamano_total= ceil(end2)-floor(inicio2)
                for k in range(us.Num_IMG-1,0,-1): ##esto va en sentido inverso, de abajo a arriba
                    initK = inicio2 +(k+1)*(inicio1-inicio2)/float(us.Num_IMG)
                    endK = end2 + (k+1)*(end1-end2)/float(us.Num_IMG)
                    long_pixel_K = (endK-initK)/float(tamano_total)
                    for t in np.arange(initK,endK,long_pixel_K):
                        rango = long_pixel_K/float(matchings[j].subA[index].longitud)
                        cont = floor(inicio1)
                        cont2 = t
                        for pixel in range (floor(t),ceil(t+long_pixel_K),1):
                            if pixel >cont2+rango:
                                cont = cont+1 
                                cont2=cont2+rango
                            R = int(row11[floor(t)][0] + (float(k+1)/float(us.Num_IMG))* (row12[cont][0]-row11[floor(t)][0]))
                            G = int(row11[floor(t)][1] + (float(k+1)/float(us.Num_IMG))* (row12[cont][1]-row11[floor(t)][1]))
                            B = int(row11[floor(t)][2] + (float(k+1)/float(us.Num_IMG))* (row12[cont][2]-row11[floor(t)][2]))
                            matrix[k+1][pixel].append((R,G,B))
                            
    

    for i in range(us.Num_IMG):
        for j in range(len(row11)-1):
            print(str(matrix[i][j]),end=" ")
        print("")
