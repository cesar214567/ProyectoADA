import sys 
sys.path.append("../")
sys.path.append("../Greedy/")
import Greedy as greed
import Useful as us
sys.path.append("../Procesamiento/")
import pil2 as pil
sys.path.append("../Animacion/")
from animacion import MostrarAnimacion

if __name__ == "__main__":
    
    #imgPath =  "../../Images/Abdullah.jpeg"
    #imgPath2 = "../../Images/Arnold_Schwarzenegger.jpg"
    imgPath =  "../../Images/Ernesto.jpeg"
    imgPath2 = "../../Images/anonymous.jpg"
    
    
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
        matchings = greed.MIN_MATCHING(a,b)
        #matchings = result[2]
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
        pil.ArmarImagen(img2,MEGA_MATRIX,i,"../../Images/IntermediasGreedy/")    
    MostrarAnimacion("../../Images/IntermediasGreedy/")

