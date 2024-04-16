from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3



class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        new_car.speed(0)
        new_car.color(random.choice(COLORS))
        new_car.goto(290, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self, increase_in_speed):
        for car in self.all_cars:
            car.forward(increase_in_speed)














