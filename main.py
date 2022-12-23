import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

slp = 0.01
num = 0
here = 1
MOVE_INCREMENT = 10
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player
player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

# controlling player
screen.listen()
screen.onkey(player.move, "Up")

# in loop
game_is_on = True
while game_is_on:
    time.sleep(slp)
    screen.update()

    if num % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # checking if player clears level
    if player.ycor() >= 300:
        here += 1
        player.goto(0, -280)
        slp *= 0.9
        car_manager.increase_speed(MOVE_INCREMENT)
        MOVE_INCREMENT += 10
        num += 2
        scoreboard.update_scoreboard(here)

    # checking if player collides with any of the vehicle
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    num += 1

screen.exitonclick()
