import pygame, os, random, math

class First_Level:
    def __init__(self, data) -> None:
        self.data = data
        self.tile_size = 30
    
    def draw(self,screen):
        for y, row in enumerate(self.data):
            for x, tile in enumerate(row):
                if tile == "#":
                    pygame.draw.rect(screen, (0,0,255), (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))