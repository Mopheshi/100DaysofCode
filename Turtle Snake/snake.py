from turtle import Turtle, Screen
import time


class Snake:
    """
    A Snake class with three circles and color them white at the center of the screen with a gap of 20
    pixels between each circle to the left of the previous circle in the snake object list and append each circle
    to the snake object list to keep track of the snake's position and movement on the screen when the snake
    moves forward by 20 pixels each time the loop runs and delay for 0.1 seconds to update the screen to show the
    snake moving forward.
    """

    def __init__(self):
        """
        Initialize the snake object with three circles and color them white
        """
        self.snakes = list()
        self.create_snake()
        self.head = self.snakes[0]
        self.game_over = False

    def create_snake(self):
        """
        Create a snake object with three circles and color them white at the center of the screen with a gap of 20
        pixels between each circle.
        :return:
        """
        for i in range(3):
            s = Turtle('circle')
            s.color('white')
            s.penup()
            s.goto(x=0 + i * -20, y=0)  # Move the snake to the left by 20 pixels each time
            self.snakes.append(s)

    def move(self):
        """
        Move the snake forward by 20 pixels
        :return:
        """
        # Start from the last snake and move backwards to the first snake
        for snake in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[snake - 1].xcor()  # Get the x coordinate of the previous snake
            y = self.snakes[snake - 1].ycor()  # Get the y coordinate of the previous snake
            self.snakes[snake].goto(x, y)  # Move the current snake to the previous snake's position
        self.snakes[0].forward(20)

    def up(self):
        """
        Move the snake up by 20 pixels
        :return:
        """
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        """
        Move the snake down by 20 pixels
        :return:
        """
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        """
        Move the snake left by 20 pixels
        :return:
        """
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        """
        Move the snake right by 20 pixels
        :return:
        """
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def refresh(self):
        """
        Refreshes the screen to show the snake moving forward and delay for 0.1 seconds each time the loop runs
        :return:
        """
        screen = Screen()
        screen.update()
        time.sleep(.2)
        self.move()
