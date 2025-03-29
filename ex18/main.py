from turtle import Screen
from player import Player
from score import Scoreboard
from car_manager import CarManager
import time

def create_window():
    window = Screen()
    window.title("Turtle Crossing Car Game")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)
    return window

screen = create_window()
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_speed = 0.1
is_game_on = True
while is_game_on:
    time.sleep(game_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.increase_level()
        game_speed *= 0.8

    for car in car_manager.cars:
        if car.distance(player.turtle) < 20:
            scoreboard.decrease_lives()
            player.reset_position()
            if scoreboard.lives == 0:
                scoreboard.game_over()
                is_game_on = False
            break

screen.exitonclick()