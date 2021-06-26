# import the libraries pygame and math
import pygame
import math


class Platform:
    BLOCK_SIZE = 64

    def __init__(self, x, y, width, height):
        # initialise the platform tiles and the width,height, x and y of the tiles as well as the number of tiles
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
        # load the tiles
        path_name = "tiles/png/Tiles/" + filename
        surface = pygame.image.load(path_name)
        # delete the white space in the tiles so that only the platform itself appears
        surface.set_colorkey(pygame.Color(255, 255, 255), pygame.RLEACCEL)
        # return the loaded tile that has been correctly scaled
        return pygame.transform.scale(surface, (self.BLOCK_SIZE, self.BLOCK_SIZE)).convert()

    def draw(self, screen):
        # set the current position
        current_pos = self.x
        num_horizontal_tiles = self.numHorizontalTiles
        # draw the left tile on the screen
        screen.blit(self.leftTile, (current_pos, self.y))
        # change the current pos
        current_pos += self.BLOCK_SIZE
        # calculate how many tiles will be needed to create a platform in the given space
        if num_horizontal_tiles > 2:
            while num_horizontal_tiles > 1:
                # draw the middle tiles
                screen.blit(self.middleTile, (current_pos, self.y))
                num_horizontal_tiles -= 1
                current_pos += self.BLOCK_SIZE
        # draw the right tile
        screen.blit(self.rightTile, (current_pos, self.y))
