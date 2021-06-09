import pygame
import spritesheet

class skeleton():
    def __init__(self):
        ss = spritesheet.spritesheet('skeleton_sheet.png')
        self.standing = ss.image_at((14, 143, 35, 48),-1)
        self.walkingLeft = ss.images_at([
            ##(15 , 78, 35, 50),
            (79, 78, 35, 50),
            (143, 78, 35, 50),
            (207, 78, 35, 50),
            (271, 78, 35, 50),
            (335, 78, 35, 50),
            (399, 78, 35, 50),
            (463, 78, 35, 50),
            (527, 78, 35, 50),
        ],-1)
        self.currentFrame = 0
        self.currentAnimation = [self.standing]
        self.x = 0
        self.y = 0
    def draw(self,screen):
        screen.blit(self.currentAnimation[self.currentFrame],(self.x,self.y))
    def walkLeft(self):
        self.direction=-1
        self.currentAnimation = self.walkingLeft

    def setPosition(self,x,y):
        self.x=x
        self.y=y
    def nextFrame(self):
        self.currentFrame = self.currentFrame+1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0

