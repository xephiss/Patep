import pygame
import spritesheet


class Coin:
    def __init__(self, x, y):
        self.still_coin = 0
        self.load_coins()
        self.current_animation = self.turning_coin
        self.current_frame = 0
        self.time_since_frame = 0
        self.time_between_frames = 5
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def load_coins(self):
        ss = spritesheet.SpriteSheet("spritesheets/coin.png")
        self.turning_coin = ss.images_at([
            (0, 0, 32, 32),
            (40, 0, 23, 32),
            (70, 0, 10, 32),
            (87, 0, 23, 32),
        ], -1)
        self.still_coin = ss.image_at((0, 0, 32, 32), -1)

    def draw(self, screen):
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
