import pygame
from game_platform import Platform
import view_port

class GameMap:
    def __init__(self):
        self.platforms = [Platform(100, 320, 256, 64),
                          Platform(400, 220, 256, 64),
                          Platform(700, 420, 256, 64),
                          Platform(1000, 620, 256, 64)]

        self.background_IMG = pygame.image.load("tiles/png/BG/BG - Copy.png").convert()
        self.background_middle_x = 0
        self.background_left_x = self.background_middle_x - 1000
        self.background_right_x = self.background_middle_x + 1000

    def draw(self,window_surface, sprite_that_falls):
        self.view_port = view_port.ViewPort(window_surface) # creates the viewport
        # checks if the x coordinate of the sprite is within the right background image panel
        if sprite_that_falls.x >= self.background_right_x:
            self.background_left_x = self.background_middle_x
            self.background_middle_x = self.background_right_x
            self.background_right_x = self.background_right_x + 1000

        elif sprite_that_falls.x <= self.background_right_x:
            self.background_right_x = self.background_middle_x
            self.background_middle_x = self.background_left_x
            self.background_left_x = self.background_left_x - 1000
        self.view_port.blit(self.background_IMG, [self.background_right_x, 0])
        self.view_port.blit(self.background_IMG, [self.background_middle_x, 0])
        self.view_port.blit(self.background_IMG, [self.background_left_x, 0])

        # iterate through the list of platforms and draw them
        for platform in self.platforms:
            platform.draw(window_surface)

    def handle_floor(self, sprite_that_falls):
        # iterate through the list of platforms and call handle_platform_floor on each platform
        for platform in self.platforms:
            self.handle_platform_floor(sprite_that_falls, platform)

    def handle_platform_floor(self, sprite_that_falls, platform):
        # check whether the sprite_that_falls that is passed into the method should be falling or not.
        # set co-ordinate for bottom of sprite
        bottom_of_sprite = sprite_that_falls.y + sprite_that_falls.height
        top_of_platform = platform.y + 2
        if platform.x <= sprite_that_falls.x <= platform.x + platform.width:
            # checks if sprite is colliding with the platform
            if top_of_platform + 5 > bottom_of_sprite > top_of_platform - 3:
                # applies the method stop_falling to the sprite_that_falls
                sprite_that_falls.gravity.stop_falling()
                sprite_that_falls.y = top_of_platform - sprite_that_falls.height - 1    # ensures the sprite lands on the platform
