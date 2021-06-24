import pygame
import math


class Platform:
    BLOCK_SIZE = 64

    def __init__(self, x, y, width, height):
        self.platformTiles = ["13.png", "14.png", "15.png"]
        self.x = x
        self.y = y
        self.height = height
        self.numHorizontalTiles = math.ceil(width / 64)
        self.width = (self.numHorizontalTiles + 0.6) * 64
        self.rightTile = self.load_tile(self.platformTiles[2])
        self.middleTile = self.load_tile(self.platformTiles[1])
        self.leftTile = self.load_tile(self.platformTiles[0])

    def load_tile(self, filename):
        path_name = "tiles/png/Tiles/" + filename
        surface = pygame.image.load(path_name)
        surface.set_colorkey(pygame.Color(255, 255, 255), pygame.RLEACCEL)
        return pygame.transform.scale(surface, (self.BLOCK_SIZE, self.BLOCK_SIZE)).convert()

    def draw(self, screen):
        current_pos = self.x
        num_horizontal_tiles = self.numHorizontalTiles
        screen.blit(self.leftTile, (current_pos, self.y))
        current_pos += self.BLOCK_SIZE
        if num_horizontal_tiles > 2:
            while num_horizontal_tiles > 1:
                screen.blit(self.middleTile, (current_pos, self.y))
                num_horizontal_tiles -= 1
                current_pos += self.BLOCK_SIZE
        screen.blit(self.rightTile, (current_pos, self.y))
