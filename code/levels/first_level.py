import pygame, os, random, math, json
class First_Level:
    def __init__(self, data) -> None:
        self.width = data["width"]
        self.height = data["height"]
        self.tiles = data["tiles"]
        self.tile_size = 30
    
    def draw(self,screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile == "#":
                    pygame.draw.rect(screen, (0,0,255), (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))