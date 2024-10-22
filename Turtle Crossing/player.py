from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_INCREMENT = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.reset()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_INCREMENT)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)
