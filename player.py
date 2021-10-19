# import the file spritesheet
import spritesheet
import pygame

# import the class Gravity from the file gravity
from gravity import Gravity
from walking import Walking
from edges import Edges


class Player(Walking, Edges):

    def __init__(self, selected_sprite):
        # this is a constructor
        self.direction = 1
        self.moving = 0

        self.time_since_frame = 0
        self.walk_speed = 8.0
        self.player_walking_speed = 30
        self.timeBetweenSteps = 1/self.player_walking_speed

        self.set_sprite(selected_sprite)

        self.current_frame = 0
        self.x = 0
        self.y = 0
        self.velocity_y = 0
        self.acceleration_y = 0
        self.gravity = Gravity(self)
        self.current_animation = self.standing
        self.num_lives = 0
        self.num_coins = 0
        self.on_ground = False

    def set_sprite(self, selected_sprite):
        # call the correct method for the object selected
        if selected_sprite == "skeleton":
            self.set_sprite_skeleton()
        elif selected_sprite == "green_dino":
            self.set_sprite_dino()

    def set_sprite_skeleton(self):
        ss = spritesheet.SpriteSheet('spritesheets/skeleton_sheet.png')
        self.standing = [ss.image_at((14, 143, 35, 48), -1)]
        self.walking = ss.images_at([
            # (15 , 78, 35, 50)
            (79, 206, 35, 50),
            (143, 206, 35, 50),
            (207, 206, 35, 50),
            (271, 206, 35, 50),
            (335, 206, 35, 50),
            (399, 206, 35, 50),
            (463, 206, 35, 50),
            (527, 206, 35, 50),
        ], -1)
        self.width = 35
        self.height = 50

    def set_sprite_dino(self):
        ss = spritesheet.SpriteSheet('spritesheets/green_dino_trimmed.png')
        self.walking = ss.images_at([
            (10, 218, 83, 91),
            (132, 218, 83, 91),
            (261, 218, 82, 91),
            (389, 218, 83, 91),
            (538, 218, 84, 91),
            (667, 218, 84, 91),
            (781, 218, 89, 91),
            (907, 218, 84, 91),
            (1034, 218, 84, 91),
        ])
        self.standing = [ss.image_at((10, 218, 83, 91))]
        self.height = 91
        self.width = 84

    def draw(self, screen):
        # draw the animation to the screen
        frame = self.current_animation[self.current_frame]
        if self.direction == -1:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self.x, self.y))

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.current_frame = self.current_frame + 1
        if self.current_frame >= len(self.current_animation):
            self.current_frame = 0
        self.x = self.x + (self.direction * self.walk_speed * self.moving)

    def update(self, time_delta):
        # updates the frames of the animation
        self.time_since_frame += time_delta
        if self.time_since_frame >= self.timeBetweenSteps:
            self.next_frame()
            self.time_since_frame -= self.timeBetweenSteps
        # handle falling
        self.gravity.update_velocity_y(time_delta)

    def jump(self):
        # makes the skeleton jump
        self.velocity_y = - 250

    def on_death(self):
        self.set_position(110, 300)
