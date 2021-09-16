import pygame


class ViewPort:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.offsetY = 0
        self.offsetX = 0
        self.width = window_surface.get_width()
        self.height = window_surface.get_height()

    def blit(self, source, dest, area=None, special_flags=0):
        # draw the object on the screen with the correct position offset
        new_dest = (dest[0] - self.offsetX, dest[1] - self.offsetY)
        return self.window_surface.blit(source, new_dest, area, special_flags)

    def centre_view_port(self, x, y):
        # creates offset based on player position on the map
        self.offsetX = x - (self.width / 2)
        self.offsetY = y - (self.height / 2)

        # Stop the view port following the player below 200 pixels, so the player can fall of the screen
        if self.offsetY > 200:
            self.offsetY = 200

    def contains(self, object):
        # check if the object is within the view_port
        return object.x + object.width > self.offsetX and object.x < self.offsetX + self.width \
               and object.y + object.height > self.offsetY and object.y < self.offsetY + self.height
