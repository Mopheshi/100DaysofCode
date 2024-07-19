import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=500)

isRaceOn = False

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter the color: ")

timmies = list()

for i in range(len(colours)):
    timmy = Turtle("turtle")
    timmy.color(colours[i])
    timmy.penup()
    timmy.goto(x=-290, y=-110 + i * 50)
    timmies.append(timmy)

if user_bet:
    isRaceOn = True

while isRaceOn:
    winner = None
    for timmy in timmies:
        if timmy.xcor() > 290:
            winner = timmy
            if winner.pencolor() == user_bet:
                print("You won!")
                isRaceOn = False
            print(f"You lost! The winner is {winner.pencolor()}...")
            isRaceOn = False
        random_distance = random.randint(0, 10)
        timmy.forward(random_distance)

screen.exitonclick()
