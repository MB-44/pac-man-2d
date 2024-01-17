import pygame, sys, time, math,json
from os import listdir;
from os.path import join, isfile;
from levels.first_level import *
from settings import *

class Game:
    def __init__(self) -> None:
        
        # setup
        pygame.init()
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
        pygame.display.set_caption("Pac Man")
        self.clock = pygame.time.Clock()
        # self.active = True

        # sprite groups

    def run(self):
        lastTime = time.time()
        
        jsonFilePath = os.path.join('code','data','first_level.json')
        
        # print(os.getcwd())
        
        # read the json file
        with open(jsonFilePath, 'r') as jsonFile:
            levelData = json.load(jsonFile)

        print(levelData)

        first_level = First_Level(levelData)

        while True:
            #delta time
            dt = time.time() - lastTime;
            lastTime = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit()
            
            # level = First_Level()
            first_level.draw(self.displaySurface)
            
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()