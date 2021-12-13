from game.action import Action
from game.coins import Coins
import raylibpy

class HandleCollisionsAction(Action):
    def __init__(self) -> None:
        super().__init__()
    
    def is_collision(self, first, second):
        x1 = first.get_position().get_x()
        y1 = first.get_position().get_y()
        width1 = first.get_width()
        height1 = first.get_height()

        rectangle1 = raylibpy.Rectangle(x1, y1, width1, height1)

        x2 = second.get_position().get_x()
        y2 = second.get_position().get_y()
        width2 = first.get_width()
        height2 = first.get_height()

        rectangle2 = raylibpy.Rectangle(x2, y2, width2, height2)

        return raylibpy.check_collision_recs(rectangle1, rectangle2)

    def handle_coin_collision(self, cast):
        coin = cast["coins"][0]
        bird = cast["bird"][0]

        if self._is_collision(bird, coin):
             # get the amount the coin is worth
             points = self.coin.get_points()
             # add to the score
             self._score_board.add_points(points)

             # get a new coin
             self._coins.reset() 