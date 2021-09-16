class Edges:
    def left_edge(self):
        return self.x

    def right_edge(self):
        return self.x + self.width

    def top_edge(self):
        return self.y

    def bottom_edge(self):
        return self.y + self.height
