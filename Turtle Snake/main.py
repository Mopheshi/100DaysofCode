from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.title('Snake')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)  # Turn off the screen updates

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while not snake.game_over:
    snake.refresh()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        # snake.extend()
        food.refresh()

screen.exitonclick()
