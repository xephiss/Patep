import pygame
import math

class Platform():
    BLOCK_SIZE = 64
    def __init__(self, x, y, width, height):
        self.platformTiles = ["13.png", "14.png", "15.png"]

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.loadTiles()


    def loadTile(self,fileName):
        pathName = "tiles/png/Tiles/" + fileName
        surface = pygame.image.load(pathName)
        surface.set_colorkey(pygame.Color(255, 255, 255), pygame.RLEACCEL)
        return pygame.transform.scale(surface,(self.BLOCK_SIZE, self.BLOCK_SIZE)).convert()

    def loadTiles(self):

        self.leftTile = self.loadTile(self.platformTiles[0])
        self.middleTile = self.loadTile(self.platformTiles[1])
        self.rightTile = self.loadTile(self.platformTiles[2])

    def draw(self, screen):
        currentPos = self.x
        numHorizontalTiles = math.ceil(self.width/64)
        screen.blit(self.leftTile, (currentPos, self.y))
        currentPos += self.BLOCK_SIZE
        if numHorizontalTiles > 2:
            while numHorizontalTiles > 1:
                screen.blit(self.middleTile, (currentPos, self.y))
                numHorizontalTiles -= 1
                currentPos += self.BLOCK_SIZE
        screen.blit(self.rightTile, (currentPos, self.y))
