
class Gravity:
    def __init__(self, object):
        # initialise the object that has been passed in
        self.object = object

    def update_velocity_y(self, time_delta):
        # update the velocity that the object moves across the y axis
        self.object.velocity_y = self.object.velocity_y + (self.object.acceleration_y * time_delta)
        self.object.y = self.object.y + (self.object.velocity_y * time_delta)

    def fall(self):
        # start the object falling
        self.object.acceleration_y = 500

    def stop_falling(self):
        # stops the object from falling
        self.object.acceleration_y = 0
        self.object.velocity_y = 0
