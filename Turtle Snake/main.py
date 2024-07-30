from turtle import Turtle, Screen

screen = Screen()
screen.title('Snake')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(8, 25)

num_snakes = 3

snakes = list()

for i in range(num_snakes):
    s = Turtle('square')
    s.color('white')
    s.penup()
    s.goto(x=0 + i * -20, y=0)
    snakes.append(s)

gameOver = False

while not gameOver:
    for snake in snakes:
        snake.forward(20)

screen.exitonclick()
