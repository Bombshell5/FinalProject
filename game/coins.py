import random
from game import constants
from game.actor import Actor
from game.point import Point

class Coins(Actor):
    """the Fish wants to get coins so it can buy a bigger fish tank. The responsibility of
    Coins is to keep track of its appearance and position. Coins can move
    around randomly if asked to do so. 
    
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self, x, y):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        # First, make sure anything from the base class gets initialized
        super().__init__()

        self.points = 0
        self.set_text("0")

        self.set_height(constants.MONEY_HEIGHT)
        self.set_width(constants.MONEY_WIDTH)
        #self.set_image(constants.IMAGE_MONEY)
        self.reset()
    
    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.
        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def reset(self):
        """
        Resets the food by moving it to a random position within the boundaries
        of the screen and reassigning the points to a random number.
        
        Args:
            self (Food): an instance of Food.
        """
        self._points = random.randint(1, 10)
        self.set_text(str(self._points))
        
        x = random.randint(20, constants.MAX_X - 20)
        y = random.randint(20, constants.MAX_Y - 20)
        position = Point(x, y)
        self.set_position(position)

