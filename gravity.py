
class Gravity:
    def __init__(self, object):
        # initialise the object that has been passed in
        self.object = object

    def update_velocity_y(self, time_delta):
        # update the velocity that the object moves across the y axis
        self.object.velocityY = self.object.velocityY + (self.object.accelerationY * time_delta)
        self.object.y = self.object.y + (self.object.velocityY * time_delta)
        print(self.object.x, ",", self.object.y)

    def fall(self):
        # start the object falling
        self.object.accelerationY = 500

    def stop_falling(self):
        # stops the object from falling
        self.object.accelerationY = 0
        self.object.velocityY = 0
