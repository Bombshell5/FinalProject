import random
#from game.move_actors_action import MoveActorsAction
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService


# TODO: Add imports similar to the following when you create these classes
from game.obstacles import Obstacles
from game.bird import Bird
from game.coins import Coins
from game.handle_input_action import HandleInputAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    
    # create the cast {key: tag, value: list}
    cast = {}
    cast["obstacles"] = []
    # TODO: Create bricks here and add them to the list

    for x in range(0, constants.MAX_X, 50):
        for y in range(0,70, 70):
            obstacle = Obstacles(x,y)
            cast["obstacles"].append(obstacle)


    cast["coins"] = []
    # TODO: Create a ball here and add it to the list
    coins = Coins(400,400)

    cast["coins"].append(coins)

    cast["bird"] = []
    # TODO: Create a paddle here and add it to the list
    bird = Bird(50,50)
    cast["bird"].append(bird)

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_input_action = HandleInputAction(input_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [handle_input_action]
    script["update"] = [move_actors_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Final Project");
  
    
    director = Director(cast, script)
    director.start_game()


if __name__ == "__main__":
    main()
