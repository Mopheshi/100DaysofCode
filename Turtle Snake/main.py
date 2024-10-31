from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title('Snake')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)  # Turn off the screen updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while not snake.game_over:
    snake.refresh()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for snake_body in snake.snakes[1:]:
        if snake.head.distance(snake_body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
