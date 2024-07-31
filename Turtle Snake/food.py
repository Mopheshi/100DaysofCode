import random
from turtle import Turtle


class Food(Turtle):
    """
    A Food class with a circle and color it blue at a random position on the screen.
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)  # 20x20 pixels (0.5x0.5 for 10x10 pixels)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
