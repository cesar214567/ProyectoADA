
#include "../Useful.cpp"
import sys
sys.path.append("../")
import Useful as us
sys.path.append("../Procesamiento")
from math import ceil,floor
import numpy as np
import pil2 as pil

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
    
    #ret2 = peso(ret1)
    ret3 = us.GetSubMatchings(ret1,A,B)
    #ret = (ret1, ret2, ret3)
    ret = (ret1,2,ret3)
    return ret


if __name__ == "__main__":
    
    imgPath =  "../../Images/Abdullah.jpeg"
    imgPath2 = "../../Images/Arnold_Schwarzenegger.jpg"
    img1 =pil.getImagenRGB(imgPath)
    img2 =pil.getImagenRGB(imgPath2)
    matriz01 = pil.convert(img1,0.2,0.6,0.2)
    matriz02 = pil.convert(img2,0.2,0.6,0.2)

    MEGA_MATRIX=[]
    for i in range(us.Num_IMG+1):
        lista_vacia=[]
        MEGA_MATRIX.append(lista_vacia)
    for i in range(len(matriz02)):
        
        row11 = pil.getRow(img1,i)
        row12 = pil.getRow(img2,i)
        a = matriz01[i]
        b = matriz02[i]
        result = MIN_MATCHING(a,b)
        matchings = result[2]
        antimatchings=us.GetAntiMatching(matchings)
        for submatching in matchings:
            submatching.getProporcionalidad
        for submatching in antimatchings:
            submatching.getProporcionalidad
        matrix=us.generarMatrizPorLinea(matchings,antimatchings,row11,row12)
        #fila original
        #iter1
        #iter2
        #fila de la otra imagen
        for j in range(len(MEGA_MATRIX)):
            MEGA_MATRIX[j].append(matrix[j])
    for i in range(us.Num_IMG+1):
        pil.ArmarImagen(img2,MEGA_MATRIX,i,"../../Images/")    
    

   
