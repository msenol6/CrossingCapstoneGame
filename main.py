from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("THE TURTLE CROSSING CAPSTONE GAME")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=player.turtle_move, key="Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    cars.build_car()
    cars.move_cars()

#detect car squish

    for cars_inlist in cars.all_cars:
        if player.distance(cars_inlist) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() >= player.end_y_position:
        player.setpos(player.starting_position)
        score.level_up()
        cars.increase_speed()

screen.exitonclick()
