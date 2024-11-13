import pandas as pd
import turtle

# squirrel_data = pd.read_csv('../Files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur_color = squirrel_data['Primary Fur Color'].value_counts()
# new_df = fur_color.to_csv('../Files/squirrel_count.csv')

us_states = pd.read_csv('../Files/50_states.csv')

screen = turtle.Screen()
screen.title('U.S. States Game')

image = '../Files/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title='Guess the State', prompt="What's another state name?").title()

guessed_states = []
while len(guessed_states) < len(us_states):
    answer_state = screen.textinput(title=f'{len(guessed_states)}/{len(us_states)} States Correct',
                                    prompt="What's another state name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in us_states.state if state not in guessed_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv('../Files/missing_states.csv')
        break

    if answer_state in us_states.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_states[us_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
