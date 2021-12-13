from game.action import Action
from game.point import Point

class HandleInputAction(Action):
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service
    
    def execute(self, cast):
        bird = cast["bird"][0]
        self._input_service

        # if one of the arrows is pressed
        # change the point of the paddle
        if self._input_service.is_up_pressed():
            x = bird.get_position().get_x()
            y = bird.get_position().get_y() 
            new_x = x 
            new_y = y - 10
            bird.set_position(Point(new_x,new_y))
        if self._input_service.is_down_pressed():
            x = bird.get_position().get_x()
            y = bird.get_position().get_y() 
            new_x = x
            new_y = y + 10
            bird.set_position(Point(new_x,new_y))
        if self._input_service.is_right_pressed():
            x = bird.get_position().get_x()
            y = bird.get_position().get_y() 
            new_x = x + 10 
            new_y = y 
            bird.set_position(Point(new_x,new_y))
        if self._input_service.is_left_pressed():
            x = bird.get_position().get_x()
            y = bird.get_position().get_y() 
            new_x = x - 10
            new_y = y 
            bird.set_position(Point(new_x,new_y))