from game.action import Action
from game.point import Point

class HandleInputAction(Action):
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service
    
    def execute(self, cast):
        paddle = cast["paddle"][0]
        self._input_service

        # if one of the arrows is pressed
        # change the point of the paddle
        if self._input_service.is_left_pressed():
            x = paddle.get_position().get_x()
            y = paddle.get_position().get_y() 
            new_x = x - 10
            new_y = y
            paddle.set_position(Point(new_x,new_y))
        if self._input_service.is_right_pressed():
            x = paddle.get_position().get_x()
            y = paddle.get_position().get_y() 
            new_x = x + 10
            new_y = y
            paddle.set_position(Point(new_x,new_y))