class Walking:
    def walk_left(self):
        # make the skeleton walk left
        self.currentAnimation = self.walking
        self.direction = -1

    def walk_right(self):
        # make the skeleton walk right
        self.currentAnimation = self.walking
        self.direction = +1

    def left_edge(self):
        return self.x + (self.width/3)

    def right_edge(self):
        return self.x + (self.width / 3 * 2)

    def set_position(self, x, y):
        # set the position of the skeleton
        self.x = x
        self.y = y