import pygame

class ViewPort:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.offsetY = 0
        self.offsetX = 0

    def blit(self,source, dest, area=None, special_flags=0):
        # draw the object on the screen with the correct position offset
        new_dest = (dest[0] - self.offsetX, dest[1] - self.offsetY)
        return self.window_surface.blit(source, new_dest, area, special_flags)

    def centre_view_port(self,x,y):
        # creates offset based on player position on the map
        self.offsetX = x - (self.window_surface.get_width() / 2)
        self.offsetY = y - (self.window_surface.get_height() / 2)