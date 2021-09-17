import pygame
from game_platform import Platform
from walking_enemy import WalkingEnemy
import spritesheet
import random


class GameMap:
    def __init__(self):
        self.Platforminstance1 = Platform(100, 420, 256, 64)
        self.platforms = [self.Platforminstance1,
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
            if platform.right_edge() + 100 > self.width:
                break
            # generate a random width of the new platform
            new_platform_width = random.randint(3, 7)*64
            # generate a random vertical position for the platform within jumping distance
            new_platform_y = random.randint(max(platform.y - 96, 0), min(platform.y + 256, self.height))
            # generate random horizontal position for the new platform within jumping distance
            # (based on height difference)
            height_difference = new_platform_y - platform.y + 96
            spacing = random.randint(45, 45 + (int(height_difference/96) * 30))
            new_platform_x = platform.right_edge() + spacing
            # append new platform to the list of platforms
            self.platforms.append(Platform(new_platform_x, new_platform_y, new_platform_width, 64))

            # if an enemy should be generated call the generate_enemy method
            if self.chance_of_enemy():
                self.generate_enemy(new_platform_x, new_platform_width, new_platform_y)

    def chance_of_enemy(self):
        # 1 in 3 chance of an enemy
        return random.randint(1, 3) == 1

    def generate_enemy(self, platform_x, platform_width, platform_y):
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
            if view_port.contains(platform):
                platform.draw(view_port)

        # iterate through the list of enemies and draw them
        for enemy in self.enemies:
            if view_port.contains(enemy):
                enemy.draw(view_port)

    def handle_floor(self, sprite_that_falls, player):
        # iterate through the list of platforms and call handle_platform_floor on each platform
        for platform in self.platforms:
            self.handle_platform_floor(sprite_that_falls, platform)
        if player:
            # check if the object is too high or too low and reset the object y value
            if sprite_that_falls.y < sprite_that_falls.height:
                sprite_that_falls.y = sprite_that_falls.height
            elif sprite_that_falls.y > 800:
                # sprite_that_falls.y = self.height
                sprite_that_falls.numLives -= 1
                sprite_that_falls.on_death()

    def handle_platform_edge(self, sprite_that_turns):
        # make the enemy turn around when it reaches the edge of the platform
        for platform in self.platforms:
            if platform.x + 5 <= sprite_that_turns.x <= platform.x + 10:
                sprite_that_turns.walk_right()
            if platform.right_edge() - 10 <= (sprite_that_turns.x + sprite_that_turns.width) <= platform.right_edge() + 5:
                sprite_that_turns.walk_left()

    def handle_platform_floor(self, sprite_that_falls, platform):
        # check whether the sprite_that_falls that is passed into the method should be falling or not.
        # set co-ordinate for bottom of object
        bottom_of_sprite = sprite_that_falls.y + sprite_that_falls.height
        top_of_platform = platform.y + 2
        if platform.x <= sprite_that_falls.right_edge() and sprite_that_falls.left_edge() <= platform.right_edge():
            # checks if object is colliding with the platform
            if top_of_platform + 5 > bottom_of_sprite > top_of_platform - 3:
                # applies the method stop_falling to the sprite_that_falls
                sprite_that_falls.gravity.stop_falling()
                # ensures the object lands on the platform
                sprite_that_falls.y = top_of_platform - sprite_that_falls.height - 1

    def detect_enemy_collision(self, player):
        # check if the player is colliding with any enemies by iterating through the list of enemies
        for enemy in self.enemies:
            if enemy.detect_collision(player):
                return True

    def end_level(self, player, window_surface):

        end_level_marker_spritesheet = spritesheet.SpriteSheet('spritesheets/skeleton_sheet.png')
        end_level_marker = end_level_marker_spritesheet.image_at((14, 143, 35, 48), -1)
        last_platform_index = len(self.platforms) - 1
        last_platform_x = self.platforms[last_platform_index].x
        last_platform_y = self.platforms[last_platform_index].y
        last_platform_width = self.platforms[last_platform_index].width
        last_platform_height = self.platforms[last_platform_index].height
        window_surface.blit(end_level_marker, (last_platform_x, last_platform_y))   # draw the end marker to the screen
        # if the player is at the same position as the end marker, the function will return True
        if player.right_edge() >= last_platform_x and player.left_edge() <= last_platform_x + last_platform_width:
            if player.bottom_edge() >= last_platform_y and player.top_edge() <= (last_platform_y + last_platform_height):
                return True

    def update(self, time_delta, view_port):
        # iterate through list of enemies
        for enemy in self.enemies:
            # check if the enemy is in the viewport
            if view_port.contains(enemy):
                # update the position of the enemy
                enemy.update(time_delta)
                # start the enemy falling
                enemy.gravity.fall()
                # check if the enemy should be falling
                self.handle_floor(enemy, False)
                self.handle_platform_edge(enemy)
