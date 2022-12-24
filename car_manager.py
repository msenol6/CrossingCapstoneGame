from turtle import Turtle
import random

colors = ["blue", "red", "yellow", "purple", "pink", "green", "gray", "orange"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5
        self.speed_up = 5

    def build_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.x_pos = self.starting_move_distance
            new_car.penup()
            self.y_pos = random.randint(-200, 200)
            new_car.goto(400, self.y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += self.speed_up
