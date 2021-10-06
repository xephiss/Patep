import spritesheet
import pygame


class Item:
    def __init(self):
        pass

    def coins(self):
        ss = spritesheet.SpriteSheet('spritesheets/coins.png')
        self.coin_sprites = ss.images_at([
            (0, 0, 32, 32),
            (40, 0, 23, 32),
            (70, 0, 10, 32),
            (87, 0, 23, 32),
        ], -1)

    def power_up(self):
        ss = spritesheet.SpriteSheet('spritesheets/gems.png')
        self.power_up_sprites = ss.images_at([
            (0, 0, 37, 32),
            (51, 0, 37, 32),
        ], -1)

    def draw(self, screen):
        # draw the animation to the screen
        frame = self.currentAnimation[self.currentFrame]
        if self.direction == -1:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self.x, self.y))

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.currentFrame = self.currentFrame + 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0
        self.x = self.x + (self.direction * self.walk_speed)

    def update(self, time_delta):
        # updates the frames of the animation
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.next_frame()
            self.timeSinceFrame -= self.timeBetweenSteps
