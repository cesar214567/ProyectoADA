import sys,pygame
from pygame.locals import *
from shutil import rmtree

sys.path.append("../")
import Useful as us
import pil

WIDTH    = 800
HEIGHT   = 600
WHITE = (255, 255, 255)

def GenerarImagenesIntermedias(img1, img2, MatrixMatchings, Directory):
    MEGA_MATRIX = []
    
    for i in range(us.Num_IMG+1):
        lista_vacia = []
        MEGA_MATRIX.append(lista_vacia)
    
    for i in range(len(MatrixMatchings)):    
        row11 = pil.getRow(img1,i)
        row12 = pil.getRow(img2,i)
        matchings = MatrixMatchings[i]

        antimatchings=us.GetAntiMatching(matchings)
        for submatching in matchings:
            submatching.getProporcionalidad()
        
        for submatching in antimatchings:
            submatching.getProporcionalidad()
        
        matrix = us.generarMatrizPorLinea(matchings,antimatchings,row11,row12)
        
        for j in range(len(MEGA_MATRIX)):
            MEGA_MATRIX[j].append(matrix[j])

    for i in range(us.Num_IMG+1):
        pil.ArmarImagen(img2, MEGA_MATRIX, i, Directory)  

def MostrarAnimacion(Directorio):
    pygame.init()
    pygame.display.set_caption('Proyecto ADA')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    cont = 1
   
    CLOCK = pygame.time.Clock()
    while True:  # main loop that runs the game            
        SURFACE.fill(WHITE)
        filename = Directorio+"imagenIntermedia"+ str(cont)+".png"
        convertedImage = pygame.image.load(filename).convert()
        SURFACE.blit(convertedImage,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                cont = 1
        CLOCK.tick(2)
        if(cont <= us.Num_IMG ):
            cont = cont + 1 

if __name__ == "__main__":
    MostrarAnimacion()