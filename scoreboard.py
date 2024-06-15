from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(x=-300, y=200)
        self.write(arg=f"level: {self.level}", align="center", font=("normal", 20, "normal"))
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(arg=f"level: {self.level}", align="center", font=("normal", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("normal", 50, "normal"))
