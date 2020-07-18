#include "../Useful.cpp"
import sys
sys.path.append("../")
import Useful as us
sys.path.append("../Procesamiento")
import pil2 as pil
A = []
B = []

def peso(matchings):
    global A
    global B
    suma_total=0
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
    ret3 = us.proporcionaliad(ret1,A,B)
    ret = (ret1 , ret2,ret3)
    return ret


if __name__ == "__main__":
    
    imgPath =  "../../Images/Abdullah.jpeg"
    imgPath2 = "../../Images/Arnold_Schwarzenegger.jpg"
    matriz01 = pil.convert(imgPath,0.2,0.6,0.2)
    matriz02 = pil.convert(imgPath2,0.2,0.6,0.2)
    img1 =pil.getImagenRGB(imgPath)
    img2 =pil.getImagenRGB(imgPath2)
    row11 = pil.getRow(img1,0)
    row12 = pil.getRow(img2,0)
    


    #a = []; 
    a = matriz01[0]
    #b = []; 
    b = matriz02[0]
    #us.Menu(a,b)
    result = MIN_MATCHING(a,b)

    for v in result[0]: 
        print("(" + str(v[0])  + "," + str(v[1]) + ") ",end = " ")

    print("\n " + str(result[1]))
    
    for submatching in result[2]: 
        submatching.printear()
    print("")
    print("")
    print("")
    print("")
    print("")

    matrix=[]
    matrix.append(row11)
    for i in range(us.Num_IMG):
        lista= []
        for j in range(len(row11)):
            R = row11[j][0]+ (float(i+1)/float(us.Num_IMG))* (row12[j][0]-row11[j][0])
            G = row11[j][1]+ (float(i+1)/float(us.Num_IMG))* (row12[j][1]-row11[j][1])
            B = row11[j][1]+ (float(i+1)/float(us.Num_IMG))* (row12[j][2]-row11[j][2])
            lista.append((R,G,B))
        matrix.append(lista)
    
    for i in range(us.Num_IMG+1):
        for j in range(len(row11)):
            print(matrix[i][j][0],end=" ")
        print("")
