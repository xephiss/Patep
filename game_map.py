import pygame
from game_platform import Platform
from walking_enemy import WalkingEnemy
import random

class GameMap:
    def __init__(self):
        self.platforms = [Platform(100, 420, 256, 64),
                          # Platform(400, 320, 256, 64),
                          # Platform(700, 520, 256, 64),
                          # Platform(1000, 720, 256, 64)
                          ]
        self.enemies = []
        self.background_IMG = pygame.image.load("tiles/png/BG/BG - Copy.png").convert()
        self.background_middle_x = 0
        self.background_left_x = self.background_middle_x - 1000
        self.background_right_x = self.background_middle_x + 1000
        self.height = 750
        self.width = 6000
        self.generate()

    def generate(self):
        # loop through list of platforms
        for platform in self.platforms:
            # if right hand edge of the platform is less then 100 pixels from the right of the end of the map, break
            if platform.x + platform.width + 100 > self.width:
                break
            # generate a random width of the new platform
            new_platform_width = random.randint(3, 7)*64
            # generate a random vertical position for the platform within jumping distance
            new_platform_y = random.randint(max(platform.y - 96, 0), min(platform.y + 256, self.height))
            # generate random horizontal position for the new platform within jumping distance (based on height difference)
            height_difference = new_platform_y - platform.y + 96
            spacing = random.randint(45, 45 + (int(height_difference/96) * 30))
            new_platform_x = platform.x + platform.width + spacing
            # append new platform to the list of platforms
            self.platforms.append(Platform(new_platform_x, new_platform_y, new_platform_width, 64))

            # if an enemy should be generated call the generateEnemy method
            if self.chanceOfEnemy():
                self.generateEnemy(new_platform_x, new_platform_width, new_platform_y)

    def chanceOfEnemy(self):
        # 1 in 3 chance of an enemy
        return random.randint(1,3) == 1

    def generateEnemy(self, platform_x, platform_width, platform_y):
        enemy = WalkingEnemy()
        random_x = random.randint(platform_x, platform_x + platform_width - enemy.width)
        enemy.set_position(random_x, platform_y - enemy.height)
        enemy.walk_left()
        self.enemies.append(enemy)

    def draw(self, view_port):
        # checks if the left edge of the viewport is within the right background image panel
        if view_port.offsetX >= self.background_right_x:
            self.background_left_x = self.background_middle_x
            self.background_middle_x = self.background_right_x
            self.background_right_x = self.background_right_x + 1000

        # checks if the left edge of the viewport is within the left background image panel
        elif view_port.offsetX <= self.background_right_x:
            self.background_right_x = self.background_middle_x
            self.background_middle_x = self.background_left_x
            self.background_left_x = self.background_left_x - 1000

        # draw background images
        view_port.blit(self.background_IMG, [self.background_right_x, 0])
        view_port.blit(self.background_IMG, [self.background_middle_x, 0])
        view_port.blit(self.background_IMG, [self.background_left_x, 0])

        # iterate through the list of platforms and draw them
        for platform in self.platforms:
            platform.draw(view_port)

        # iterate through the list of enemies and draw them
        for enemy in self.enemies:
            enemy.draw(view_port)

    def handle_floor(self, sprite_that_falls):
        # iterate through the list of platforms and call handle_platform_floor on each platform
        for platform in self.platforms:
            self.handle_platform_floor(sprite_that_falls, platform)

        # check if the sprite is too high or too low and reset the sprite y value
        if sprite_that_falls.y < sprite_that_falls.height:
            sprite_that_falls.y = sprite_that_falls.height
        elif sprite_that_falls.y > self.height:
            sprite_that_falls.y = self.height

    def handle_platform_floor(self, sprite_that_falls, platform):
        # check whether the sprite_that_falls that is passed into the method should be falling or not.
        # set co-ordinate for bottom of sprite
        bottom_of_sprite = sprite_that_falls.y + sprite_that_falls.height
        top_of_platform = platform.y + 2
        if platform.x <= sprite_that_falls.right_edge() and sprite_that_falls.left_edge() <= platform.x + platform.width:
            # checks if sprite is colliding with the platform
            if top_of_platform + 5 > bottom_of_sprite > top_of_platform - 3:
                # applies the method stop_falling to the sprite_that_falls
                sprite_that_falls.gravity.stop_falling()
                sprite_that_falls.y = top_of_platform - sprite_that_falls.height - 1   # ensures the sprite lands on the platform

    def update(self,time_delta):
        # iterate through list of enemies
        for enemy in self.enemies:
            #update the postiion of the enemy
            enemy.update(time_delta)
            # start the enemy falling
            enemy.gravity.fall()
            # check if the enemy should be falling
            self.handle_floor(enemy)