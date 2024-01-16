import pygame, sys, time, math;
from os import listdir;
from os.path import join, isfile;
from settings import *
class Game:
    def __init__(self) -> None:
 
        # setup
        pygame.init()
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
        pygame.display.set_caption("Pac Man")
        self.clock = pygame.time.Clock()
        self.active = True

        # sprite groups
        




    def run(self):
        lastTime = time.time()
        
        while True:
            #delta time
            dt = time.time() - lastTime;
            lastTime = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit()
                if event.type == pygame.K_UP:
                    pass
                if event.type == pygame.K_DOWN:
                    pass
                if event.type == pygame.K_LEFT:
                    pass
                if event.type == pygame.K_RIGHT:
                    pass







if __name__ == "__main__":
    game = Game()
    game.run()