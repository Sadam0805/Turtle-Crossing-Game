from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_again()
        self.left(90)

    def go_up(self):
        self.forward(10)

    def start_again(self):
        self.goto(x=0, y=-230)

    def finish_line(self):
        if self.ycor() > 235:
            return True
        else:
            return False
