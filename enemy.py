class Enemy:
    def left_edge(self):
        return self.x

    def right_edge(self):
        return self.x + self.width

    def top_edge(self):
        return self.y

    def bottom_edge(self):
        return self.y + self.height

    def detect_collision(self, player):
        playerLeftEdge = player.x
        playerRightEdge = player.x + player.width
        playerTopEdge = player.y
        playerBottomEdge = player.y + player.height

        if playerRightEdge >= self.left_edge() and playerLeftEdge <= self.right_edge():
            if playerBottomEdge >= self.top_edge() and playerTopEdge <= self.bottom_edge():
                return True

