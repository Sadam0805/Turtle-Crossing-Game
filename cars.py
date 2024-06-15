from turtle import Turtle
import random


class Cars:
    def __init__(self):
        self.colors = ["yellow", "purple", "green", "red", "orange", "blue", "pink"]
        self.all_cars = []
        self.car_speed = 5

    def creating_car(self):
        creating = random.randint(1, 6)
        if creating == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            new_y = random.randint(-200, 200)
            car.color(random.choice(self.colors))
            car.goto(x=400, y=new_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level(self):
        self.car_speed += 5
