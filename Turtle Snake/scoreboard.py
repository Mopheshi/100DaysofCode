from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'bold')


class Scoreboard(Turtle):
    """
    A Scoreboard class with a turtle object to display the score at the top of the screen.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current score
        :return:
        """
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score by 1
        :return:
        """
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Display the game over a message on the screen
        :return:
        """
        self.goto(0, 0)
        self.write('YIKES...\n', align=ALIGNMENT, font=FONT)
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)
