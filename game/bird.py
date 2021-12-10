
from game.actor import Actor
from game.point import Point
from game import constants

class Bird(Actor):
    def __init__(self, x, y):

        super().__init__()

        self.set_width(constants.BIRD_WIDTH)
        self.set_height(constants.BIRD_HEIGHT)
        position = Point(x,y)
        self.set_position(position)
        self.set_image(constants.IMAGE_BIRD)

