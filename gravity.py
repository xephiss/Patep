
class Gravity:
    def __init__(self, object):
        self.object = object

    def update_velocity_y(self, time_delta):
        self.object.velocityY = self.object.velocityY + (self.object.accelerationY * time_delta)
        self.object.y = self.object.y + (self.object.velocityY * time_delta)

    def fall(self):
        self.object.accelerationY = 25

    def stop_falling(self):
        self.object.accelerationY = 0
        self.object.velocityY = 0
