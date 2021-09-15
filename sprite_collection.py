# import the library pygame
import pygame


class SpriteCollection(object):
    def __init__(self, directoryName, width, height):
        self.directoryName = directoryName
        self.width = width
        self.height = height

    def single_image(self, fileName, colorkey):
        try:
            image = pygame.image.load(self.directoryName + "/" + fileName).convert_alpha()
        except pygame.error as message:
            print('Unable to load object image:', fileName)
            raise SystemExit(message)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            # image.set_colorkey(colorkey, pygame.RLEACCEL)
        return pygame.transform.scale(image, (self.width, self.height))