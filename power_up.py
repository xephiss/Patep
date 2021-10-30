import spritesheet
from edges import Edges


class PowerUp(Edges):
    def __init__(self, x, y):
        self.load_power_ups()
        self.x = x
        self.y = y
        self.width = 37
        self.height = 32
        self.collected = False

    def load_power_ups(self):
        ss = spritesheet.SpriteSheet("spritesheets/coin.png")
        self.power_up = ss.image_at([51, 0, 37, 32], -1)

    def draw(self, screen):
        if not self.collected:
            # draw the animation to the screen
            frame = self.power_up
            screen.blit(frame, (self.x, self.y))

    def detect_collision(self, player):
        if not self.collected:
            if player.right_edge() >= self.left_edge() and player.left_edge() <= self.right_edge():
                if player.bottom_edge() >= self.top_edge() and player.top_edge() <= self.bottom_edge():
                    return True

    def hide(self):
        self.collected = True
