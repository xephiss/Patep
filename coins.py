import pygame
import spritesheet


class Coin:
    def __init__(self, x, y):
        self.turning_coin = []
        self.still_coin = 0
        self.currentAnimation = self.turning_coin
        self.currentFrame = 0
        self.timeSinceFrame = 0
        self.timeBetweenSteps = 0
        self.x = x
        self.y = y

    def load_coins(self):
        ss = spritesheet.SpriteSheet("spritesheets/coin.png")
        self.turning_coin = ss.images_at([

        ])
        self.still_coin = ss.image_at()

    def draw(self, screen):
        # draw the animation to the screen
        frame = self.currentAnimation[self.currentFrame]
        screen.blit(frame, (self.x, self.y))

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.currentFrame = self.currentFrame + 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0

    def update(self, time_delta):
        # updates the frames of the animation
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.next_frame()
            self.timeSinceFrame -= self.timeBetweenSteps
