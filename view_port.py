class ViewPort:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.offset_y = 0
        self.offset_x = 0
        self.width = window_surface.get_width()
        self.height = window_surface.get_height()

    def blit(self, source, dest, area=None, special_flags=0):
        # draw the object on the screen with the correct position offset
        new_dest = (dest[0] - self.offset_x, dest[1] - self.offset_y)
        return self.window_surface.blit(source, new_dest, area, special_flags)

    def centre_view_port(self, x, y):
        # creates offset based on player position on the map
        self.offset_x = x - (self.width / 2)
        self.offset_y = y - (self.height / 2)

        # Stop the view port following the player below 200 pixels, so the player can fall of the screen
        if self.offset_y > 200:
            self.offset_y = 200

    def contains(self, object):
        # check if the object is within the view_port
        return object.x + object.width > self.offset_x and object.x < self.offset_x + self.width \
               and object.y + object.height > self.offset_y and object.y < self.offset_y + self.height
