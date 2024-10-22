import time
from turtle import Screen

from scoreboard import ScoreBoard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

gameOver = False

while not gameOver:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            gameOver = True
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
