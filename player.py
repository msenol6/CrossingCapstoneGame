from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.starting_position = (0, -300)
        self.setpos(self.starting_position)
        self.end_y_position = 300

    def turtle_move(self):
        self.forward(10)
