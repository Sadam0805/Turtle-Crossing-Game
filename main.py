from turtle import Screen
from my_turtle import MyTurtle
from cars import Cars
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)

turtle = MyTurtle()
screen.onkey(fun=turtle.go_up, key="Up")

cars = Cars()

scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.creating_car()
    cars.move_cars()

    for player in cars.all_cars:
        if turtle.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.finish_line():
        turtle.start_again()
        cars.level()
        scoreboard.level_up()

screen.exitonclick()
