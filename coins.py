import pygame
import spritesheet
from edges import Edges


class Coin(Edges):
    def __init__(self, x, y):
        self.still_coin = 0
        self.load_coins()
        self.current_animation = self.turning_coin
        self.current_frame = 0
        self.time_since_frame = 0
        self.time_between_frames = 0.25
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.collected = False

    def load_coins(self):
        ss = spritesheet.SpriteSheet("spritesheets/coin.png")
        self.turning_coin = ss.images_at([
            (0, 0, 32, 32),
            (36, 0, 32, 32),
            (69, 0, 32, 32),
            (100, 0, 32, 32),
        ], -1)
        self.still_coin = ss.image_at((0, 0, 32, 32), -1)

    def draw(self, screen):
        if not self.collected:
            # draw the animation to the screen
            frame = self.current_animation[self.current_frame]
            screen.blit(frame, (self.x, self.y))

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.current_frame = self.current_frame + 1
        if self.current_frame >= len(self.current_animation):
            self.current_frame = 0

    def update(self, time_delta):
        # updates the frames of the animation
        self.time_since_frame += time_delta
        if self.time_since_frame >= self.time_between_frames:
            self.next_frame()
            self.time_since_frame -= self.time_between_frames

    def detect_collision(self, player):
        if not self.collected:
            if player.right_edge() >= self.left_edge() and player.left_edge() <= self.right_edge():
                if player.bottom_edge() >= self.top_edge() and player.top_edge() <= self.bottom_edge():
                    return True

    def hide(self):
        self.collected = True