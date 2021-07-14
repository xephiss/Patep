import pygame
from game_platform import Platform


class GameMap:
    def __init__(self):
        self.platforms = [Platform(100, 320, 256, 64),
                          Platform(400, 220, 256, 64),
                          Platform(700, 420, 256, 64),
                          Platform(1000, 620, 256, 64)]

    def draw(self,window_surface):
        for platform in self.platforms:
            platform.draw(window_surface)

    def handle_floor(self,sprite_that_falls):
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