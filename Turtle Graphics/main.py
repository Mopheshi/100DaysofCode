import random
import turtle
from turtle import Turtle, Screen
from extract_colour import colours

turtle.colormode(255)

timmy = Turtle()
timmy.shape('turtle')
timmy.color('LimeGreen')
timmy.speed('fastest')

colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'pink', 'brown', 'cyan']


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(50)
        timmy.right(angle)


def draw_dashed_line():
    for i in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw_shapes(num):
    # random = Random()
    # intColor = random.randint(0, len(colors) - 1)
    for i in range(3, num):
        # timmy.color(colors[intColor])
        timmy.color(random_color())
        draw_shape(i)


def random_square_walk(num):
    timmy.pensize(10)
    timmy.speed(50)
    # timmy.hideturtle()
    directions = [0, 90, 180, 270]
    for i in range(num):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))


def random_walk(num, maxDistance):
    for i in range(num):
        randomAngle = random.randint(0, 360)
        randomDistance = random.randint(0, maxDistance)
        timmy.color(random_color())
        timmy.setheading(randomAngle)
        timmy.forward(randomDistance)


def draw_circle():
    for i in range(36):
        timmy.forward(10)
        timmy.right(10)


def draw_spirograph(gapSize):
    for i in range(int(360 / gapSize)):
        timmy.color(random_color())
        # draw_circle()
        timmy.circle(100)
        # timmy.right(gapSize)
        timmy.setheading(timmy.heading() + gapSize)


def draw_scattered_dots():
    for i in range(100):
        timmy.penup()
        timmy.goto(random.randint(-300, 300), random.randint(-300, 300))
        timmy.pendown()
        timmy.dot(random.randint(10, 50), random_color())


def draw_dot():
    timmy.dot(20, random_color())


def hirst_painting(rows, columns):
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(-300, -300)
    # timmy.pendown()
    for i in range(rows):
        for j in range(columns):
            timmy.color(random.choice(colours))
            timmy.dot(20)
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        timmy.penup()
        timmy.goto(-300, timmy.ycor() + 50)
        timmy.pendown()


hirst_painting(10, 10)

screen = Screen()
screen.exitonclick()
