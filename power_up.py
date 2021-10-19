import spritesheet


class PowerUp:
    def __init__(self, x, y):
        self.turning_coin = []
        self.still_coin = 0
        self.current_animation = self.power_up_sprites
        self.current_frame = 0
        self.time_since_frame = 0
        self.time_between_steps = 0
        self.x = x
        self.y = y

    def load_power_up(self):
        ss = spritesheet.SpriteSheet('spritesheets/gems.png')
        self.power_up_sprites = ss.images_at([
            (0, 0, 37, 32),
            (51, 0, 37, 32),
        ], -1)

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
        if self.time_since_frame >= self.time_between_steps:
            self.next_frame()
            self.time_since_frame -= self.time_between_steps