from turtle import Screen
from snake import Snake

screen = Screen()
screen.title('Snake')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)  # Turn off the screen updates

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while not snake.game_over:
    snake.refresh()
    snake.move()

screen.exitonclick()
