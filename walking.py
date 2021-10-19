class Walking:
    def walk_left(self):
        # make the sprite walk left
        self.current_animation = self.walking
        self.direction = -1
        self.moving = 1

    def walk_right(self):
        # make the sprite walk right
        self.current_animation = self.walking
        self.direction = +1
        self.moving = 1

    def stop_walking(self):
        # stop walking
        self.current_animation = self.standing
        self.current_frame = 0
        self.moving = 0

    def left_edge(self):
        return self.x + (self.width/3)

    def right_edge(self):
        return self.x + (self.width / 3 * 2)

    def set_position(self, x, y):
        # set the position of the skeleton
        self.x = x
        self.y = y