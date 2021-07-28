# import the file spritesheet
import spritesheet
import sprite_collection

# import the class Gravity from the file gravity
from gravity import Gravity


class Player:
    def __init__(self):
        self.direction = 0

        self.timeSinceFrame = 0
        self.playerWalkingSpeed = 20
        self.timeBetweenSteps = 1/self.playerWalkingSpeed

        self.set_sprite_skeleton()
        #self.set_sprite_dino()

        self.currentFrame = 0
        self.currentAnimation = [self.standing]
        self.x = 0
        self.y = 0
        self.velocityY = 0
        self.accelerationY = 0
        self.width = 35
        self.height = 50
        self.gravity = Gravity(self)
        self.standing = None
        self.walkingLeft = None
        self.walkingRight = None

    def set_sprite_skeleton(self):
        ss = spritesheet.SpriteSheet('skeleton_sheet.png')
        self.standing = ss.image_at((14, 143, 35, 48), -1)
        self.walkingLeft = ss.images_at([
            # (15 , 78, 35, 50)
            (79, 78, 35, 50),
            (143, 78, 35, 50),
            (207, 78, 35, 50),
            (271, 78, 35, 50),
            (335, 78, 35, 50),
            (399, 78, 35, 50),
            (463, 78, 35, 50),
            (527, 78, 35, 50),
        ], -1)
        self.walkingRight = ss.images_at([
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

    def set_sprite_dino(self):
        ss = spritesheet.SpriteSheet('green_dino_trimmed.png')
        self.walkingRight = ss.images_at([
            (10, 218, 83, 91),
            (132, 218, 83, 91),
            (261, 218, 82, 91),
            (389, 218, 83, 91),
            (538, 218, 84, 91),
            (667, 218, 84, 91),
            (781, 218, 89, 91),
            (907, 218, 84, 91),
            (1034, 218, 84, 91),
        ], -1)
        self.walkingLeft = [self.walkingRight[0]]
        self.standing = ss.image_at([(10, 218, 83, 91)],-1)

    def draw(self, screen):
        # draw the animation to the screen
        print(self.currentFrame)
        print(len(self.currentAnimation))
        screen.blit(self.currentAnimation[self.currentFrame], (self.x, self.y))

    def walk_left(self):
        # make the skeleton walk left
        self.direction = -1
        self.currentAnimation = self.walkingLeft

    def set_position(self, x, y):
        # set the position of the skeleton
        self.x = x
        self.y = y

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.currentFrame = self.currentFrame + 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0
        self.x = self.x + (self.direction * 3)

    def walk_right(self):
        # make the skeleton walk right
        self.currentAnimation = self.walkingRight
        self.direction = +1

    def update(self, time_delta):
        # updates the frames of the animation
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.next_frame()
            self.timeSinceFrame = 0
        # handle falling
        self.gravity.update_velocity_y(time_delta)

    def jump(self):
        # makes the skeleton jump
        self.velocityY = - 250

