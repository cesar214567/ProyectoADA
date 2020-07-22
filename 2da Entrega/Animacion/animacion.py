import sys,pygame
sys.path.append("../")
from Useful import Num_IMG
from pygame.locals import *
from shutil import rmtree
WIDTH    = 800
HEIGHT   = 600
WHITE = (255, 255, 255)
def MostrarAnimacion(Directorio):

    pygame.init()
    pygame.display.set_caption('Proyecto ADA')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    cont = 1
   
    CLOCK = pygame.time.Clock()
    while True:  # main loop that runs the game            
        SURFACE.fill(WHITE)
        filename = Directorio+"imagenIntermedia"+ str(cont)+".png"
        print(filename)
        convertedImage = pygame.image.load(filename).convert()
        SURFACE.blit(convertedImage,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                try:
                    rmtree(Directorio)
                except:
                    pass
                sys.exit()
            if event.type == KEYDOWN:
                cont = 1
        CLOCK.tick(2)
        if(cont <= Num_IMG ):
            cont = cont + 1 

if __name__ == "__main__":
    MostrarAnimacion()
    # GAA