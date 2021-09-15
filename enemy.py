from edges import Edges


class Enemy(Edges):

    def detect_collision(self, player):
        if player.right_edge() >= self.left_edge() and player.left_edge() <= self.right_edge():
            if player.bottom_edge() >= self.top_edge() and player.top_edge() <= self.bottom_edge():
                return True
