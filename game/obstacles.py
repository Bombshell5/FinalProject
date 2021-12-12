import raylibpy
from game.actor import Actor
from game.point import Point
from game import constants

class Obstacles(Actor):
    def __init__(self, x, y):

        super().__init__()

        self.set_width(constants.OBSTACLE_WIDTH)
        self.set_height(constants.OBSTACLE_HEIGHT)
        position = Point(x,y)
        self.set_position(position)
        self.set_image(constants.IMAGE_OBSTACLE)

    def set_position(self, position):
        return super().set_position(position)

    def get_position(self):
        return super().get_position()