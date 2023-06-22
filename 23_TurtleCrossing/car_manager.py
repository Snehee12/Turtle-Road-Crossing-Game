from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]

    def create_cars(self):
        while randint(1,6)==1:
            newcar=Turtle()
            newcar.shape("square")
            newcar.shapesize(stretch_len=2)
            newcar.penup()
            newcar.color(choice(COLORS))
            y_position=randint(-250,250)
            newcar.goto(300,y_position)
            self.all_cars.append(newcar)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)