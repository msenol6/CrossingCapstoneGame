from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-350, 290)
        self.update_score()

    def update_score(self):
        # align'den once true dersek bir sonraki leveli uzerine degil yan,na bastiriyor
        self.write(f"Level: {self.level}",  align="left", font=("Arial", 12, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
