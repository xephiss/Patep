import pygame
from game_platform import Platform
from walking_enemy import WalkingEnemy
from coins import Coin
import spritesheet
import random


class GameMap:
    def __init__(self):
        self.platform_instance1 = Platform(100, 420, 256, 64)
        self.platforms = [self.platform_instance1, ]
        self.enemies = []
        self.coins = []
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

            # generate the coins
            self.generate_coins(new_platform_x, new_platform_width , new_platform_y)

            self.create_end_level_marker()

    def chance_of_enemy(self):
        # 1 in 3 chance of an enemy
        return random.randint(1, 3) == 1

    def chance_of_coin(self):
        # 1 in 2 chance of an enemy
        return random.randint(1, 2) == 1

    def generate_enemy(self, platform_x, platform_width, platform_y):
        # create instance of class WalkingEnemy
        enemy = WalkingEnemy()
        # get a random x coordinate on the platform
        random_x = random.randint(platform_x, platform_x + platform_width - enemy.width)
        # set the position of the new enemy object
        enemy.set_position(random_x, platform_y - enemy.height)
        # start the enemy walking left
        enemy.walk_left()
        # append the enemy to the list of enemies
        self.enemies.append(enemy)

    def generate_coins(self, platform_x, platform_width, platform_y):
        coin_x = platform_x + 16
        while coin_x < platform_x + platform_width:
            if self.chance_of_coin():
                # set random y position of coin to somewhere above the platform in reach of player
                random_y = random.randint(platform_y - 110, platform_y - 32)
                # create instance of class Coin
                coin = Coin(coin_x, random_y)
                # appened the coin to the list of coins
                self.coins.append(coin)
            coin_x += 64

    def draw(self, view_port):
        # checks if the left edge of the viewport is within the right background image panel
        if view_port.offset_x > self.background_right_x:
            self.background_left_x = self.background_middle_x
            self.background_middle_x = self.background_right_x
            self.background_right_x = self.background_right_x + 1000

        # checks if the left edge of the viewport is within the left background image panel
        elif view_port.offset_x < self.background_middle_x:
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

        # iterate through the lise of coins and draw them
        for coin in self.coins:
            if view_port.contains(coin):
                coin.draw(view_port)

        # iterate through the list of enemies and draw them
        for enemy in self.enemies:
            if view_port.contains(enemy):
                enemy.draw(view_port)

        self.draw_end_level_marker(view_port)

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
                sprite_that_falls.num_lives -= 1
                sprite_that_falls.on_death()

    def handle_platform_edge(self, sprite_that_turns):
        # make the enemy turn around when it reaches the edge of the platform
        for platform in self.platforms:
            if platform.x <= sprite_that_turns.x <= platform.x + 10:
                sprite_that_turns.walk_right()
            if platform.right_edge() - 10 <= (sprite_that_turns.x + sprite_that_turns.width) <= platform.right_edge():
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
                sprite_that_falls.on_ground = True

    def detect_enemy_collision(self, player):
        # check if the player is colliding with any enemies by iterating through the list of enemies
        for enemy in self.enemies:
            if enemy.detect_collision(player):
                return True

    def draw_end_level_marker(self, view_port):
        end_level_marker_spritesheet = spritesheet.SpriteSheet('spritesheets/portal.png')
        end_level_marker = end_level_marker_spritesheet.image_at((0, 0, 74, 81))
        view_port.blit(end_level_marker, (self.end_level_x, self.end_level_y))  # draw the end marker to the screen

    def create_end_level_marker(self):
        last_platform_index = len(self.platforms) - 1
        last_platform = self.platforms[last_platform_index]
        self.end_level_x = last_platform.x + (last_platform.width/2)
        self.end_level_y = last_platform.y - 85

    def end_level(self, player):
        # if the player is at the same position as the end marker, the function will return True
        if player.right_edge() >= self.end_level_x:
            if player.bottom_edge() <= self.end_level_y + 100:
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
        # iterate through list of coins
        for coin in self.coins:
            # check if the coin is in the viewport
            if view_port.contains(coin):
                # update the coin
                coin.update(time_delta)
