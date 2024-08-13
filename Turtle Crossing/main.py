import time
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

gameOver = False

while not gameOver:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
