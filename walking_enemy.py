import spritesheet
import pygame
from gravity import Gravity
from walking import Walking
from enemy import Enemy


class WalkingEnemy(Walking, Enemy):
    def __init__(self):
        self.direction = 1
        self.moving = 0
        self.x = 0
        self.y = 0
        self.set_sprite()
        self.current_animation = self.standing
        self.current_frame = 0
        self.gravity = Gravity(self)
        self.velocity_y = 0
        self.acceleration_y = 0
        self.time_since_frame = 0
        self.player_walking_speed = 10
        self.time_between_steps = 1 / self.player_walking_speed

    def set_sprite(self):
        ss = spritesheet.SpriteSheet('spritesheets/green_trex.png')
        self.walking = ss.images_at([
            (5, 227, 121, 86),
            (176, 227, 121, 86),
            (340, 227, 120, 86),
            (511, 227, 121, 86),
            (681, 227, 122, 86),
            (864, 227, 121, 86),
            (1035, 227, 122, 86),
            (1217, 227, 122, 86),
            (1388, 227, 122, 86)
        ])
        self.standing = [ss.image_at((6, 0, 122, 79))]
        self.height = 86
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
        self.x = self.x + (self.direction * 3 * self.moving)
        # update height every time

    def update(self, time_delta):
        # updates the frames of the animation
        self.time_since_frame += time_delta
        if self.time_since_frame >= self.time_between_steps:
            self.next_frame()
            self.time_since_frame -= self.time_between_steps
        # handle falling
        self.gravity.update_velocity_y(time_delta)
