from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="space", fun=clear_screen)
screen.exitonclick()
