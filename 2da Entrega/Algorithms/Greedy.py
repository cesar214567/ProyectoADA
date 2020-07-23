
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
    return ret3





