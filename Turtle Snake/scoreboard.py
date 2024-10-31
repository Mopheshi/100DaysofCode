from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')


def read_highscore():
    with open('../Files/highscore.txt', mode='r') as file:
        return int(file.read())


def write_highscore(score):
    with open('../Files/highscore.txt', mode='w') as file:
        return file.write(str(score))


class Scoreboard(Turtle):
    """
    A Scoreboard class with a turtle object to display the score at the top of the screen.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = read_highscore()
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
        self.write(f'Score: {self.score} High Score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score by 1
        :return:
        """
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     Display the game over a message on the screen
    #     :return:
    #     """
    #     self.goto(0, 0)
    #     self.write('YIKES...\n', align=ALIGNMENT, font=FONT)
    #     self.write('GAME OVER!', align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Reset the score to 0
        :return:
        """
        if self.score > self.highscore:
            self.highscore = self.score
            write_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()
