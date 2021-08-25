import spritesheet
import pygame
from gravity import Gravity
from walking import Walking

class WalkingEnemy(Walking):
    def __init__(self):
        self.direction = 0
        self.x = 0
        self.y = 0
        self.set_sprite()
        self.currentAnimation = [self.standing]
        self.currentFrame = 0
        self.gravity = Gravity(self)
        self.velocityY = 0
        self.accelerationY = 0
        self.timeSinceFrame = 0
        self.playerWalkingSpeed = 20
        self.timeBetweenSteps = 1 / self.playerWalkingSpeed

    def set_sprite(self):
        ss = spritesheet.SpriteSheet('spritesheets/green_trex.png')
        self.walking = ss.images_at([
            (5,233 ,121 ,80 ),
            (176, 230, 121, 83),
            (340,227 ,120 ,86 ),
            (511, 231, 121,82 ),
            (681,233 ,122 ,80 ),
            (864,231 ,121 ,82 ),
            (1035 ,231 ,122, 82),
            (1217, 232, 122, 81),
            (1388, 233, 122, 80),
            (0, 339, 121, 79),
            (130, 329, 112, 89),
            (272, 318, 105, 100),
            (408, 337, 115, 81),
            (567, 352, 122, 66),
            (738, 354, 122, 64),
            (920, 355, 122, 63),
            (1107, 350, 123, 68),
            (1299, 345, 122, 73),
            (1463, 339, 121, 79),
        ])
        self.standing = ss.image_at((6, 0, 122, 79))
        self.height = 91
        self.width = 84

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
        self.x = self.x + (self.direction * 3)

    def update(self, time_delta):
        # updates the frames of the animation
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.next_frame()
            self.timeSinceFrame -= self.timeBetweenSteps
        # handle falling
        self.gravity.update_velocity_y(time_delta)