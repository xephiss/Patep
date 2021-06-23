import spritesheet

class Skeleton:
    def __init__(self):
        self.direction = 1
        ss = spritesheet.spritesheet('skeleton_sheet.png')
        self.standing = ss.image_at((14, 143, 35, 48), -1)
        self.timeSinceFrame = 0
        self.skeletonWalkingSpeed = 0.125
        self.walkingLeft = ss.images_at([
            # (15 , 78, 35, 50),#
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
            # (15 , 78, 35, 50),#
            (79, 206, 35, 50),
            (143, 206, 35, 50),
            (207, 206, 35, 50),
            (271, 206, 35, 50),
            (335, 206, 35, 50),
            (399, 206, 35, 50),
            (463, 206, 35, 50),
            (527, 206, 35, 50),
        ], -1)
        self.currentFrame = 0
        self.currentAnimation = [self.standing]
        self.x = 0
        self.y = 0
        self.velocityY = 0
        self.accelerationY = 0
        self.width = 35
        self.height = 50

    def draw(self, screen):
        screen.blit(self.currentAnimation[self.currentFrame], (self.x, self.y))

    def walk_left(self):
        self.direction = -1
        self.currentAnimation = self.walkingLeft

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def next_frame(self):
        self.currentFrame = self.currentFrame+1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0
        self.x = self.x + (self.direction*3)

    def walk_right(self):
        self.currentAnimation = self.walkingRight

    def update(self,time_delta):
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.skeletonWalkingSpeed:
            self.next_frame()
            self.timeSinceFrame = 0
        self.velocityY = self.velocityY + (self.accelerationY * time_delta)
        self.y = self.y + (self.velocityY * time_delta)

    def fall(self):
        self.accelerationY = 25


    def stop_falling(self):
        self.accelerationY = 0
        self.velocityY = 0

