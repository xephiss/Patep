# import the libraries pygame and math
import pygame
import math

from edges import Edges


class Platform(Edges):
    BLOCK_SIZE = 64

    def __init__(self, x, y, width, height):
        # initialise the platform tiles and the width,height, x and y of the tiles as well as the number of tiles
        self.platform_tiles = ["13.png", "14.png", "15.png"]
        self.x = x
        self.y = y
        self.height = height
        # ensures the platform will always be at least as wide as the specified width
        self.num_horizontal_tiles = math.ceil(width / self.BLOCK_SIZE)
        # calculates the resulting width of the platform
        self.width = (self.num_horizontal_tiles + 1) * self.BLOCK_SIZE
        self.right_tile = self.load_tile(self.platform_tiles[2])
        self.middle_tile = self.load_tile(self.platform_tiles[1])
        self.left_tile = self.load_tile(self.platform_tiles[0])

    def load_tile(self, filename):
        # load the tiles
        path_name = "tiles/png/Tiles/" + filename
        surface = pygame.image.load(path_name)
        # delete the white space in the tiles so that only the platform itself appears
        surface.set_colorkey(pygame.Color(255, 255, 255), pygame.RLEACCEL)
        # return the loaded tile that has been correctly scaled
        return pygame.transform.scale(surface, (self.BLOCK_SIZE, self.BLOCK_SIZE)).convert()

    def draw(self, screen):
        current_pos = self.x  # set the current position
        num_horizontal_tiles = self.num_horizontal_tiles

        screen.blit(self.left_tile, (current_pos, self.y))  # draw the left tile on the screen

        current_pos += self.BLOCK_SIZE  # change the current position to the new position
        # calculate how many tiles will be needed to create a platform in the given space
        if num_horizontal_tiles > 2:
            while num_horizontal_tiles > 1:
                # draw the middle tiles
                screen.blit(self.middle_tile, (current_pos, self.y))
                num_horizontal_tiles -= 1
                current_pos += self.BLOCK_SIZE
        screen.blit(self.right_tile, (current_pos, self.y))  # draw the right tile
