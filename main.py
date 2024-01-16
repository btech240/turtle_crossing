import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()

screen.listen()

# Left paddle control
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.gameover()

    if player.ycor() > 280:
        score.new_level()
        time.sleep(1)
        player.new_level()
        car_manager.level_up()


# Prevent exit until click
screen.exitonclick()
