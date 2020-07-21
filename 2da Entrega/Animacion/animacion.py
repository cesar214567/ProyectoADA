import sys,pygame
sys.path.append("../")
from Useful import Num_IMG
from pygame.locals import *
WIDTH    = 800
HEIGHT   = 600
WHITE = (255, 255, 255)
DirectorioDinamica = ""
DirectorioGreedy = "../../Images/IntermediasGreedy/"
DirectorioMejorada = ""

def MostrarAnimacion():
    pygame.init()
    pygame.display.set_caption('Proyecto ADA')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    cont = 1
   
    CLOCK = pygame.time.Clock()
    while True:  # main loop that runs the game            
        SURFACE.fill(WHITE)
        filename = DirectorioGreedy+"imagenIntermedia"+ str(cont)+".png"
        print(filename)
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
        if(cont <= Num_IMG ):
            cont = cont + 1 

if __name__ == "__main__":
    MostrarAnimacion()
    # GAA