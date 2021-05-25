import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Guessing Game")
img_file = "blank_states_img.gif"
screen.addshape(img_file)
turtle.shape(img_file)
df = pd.read_csv("50_states.csv")
df['state'] = df.state.apply(lambda x: x.lower())
total_states = len(df)
correct_answers = dict()

def get_state_coordinates(answer):
    print(answer, df[['x', 'y']])

    if not df['state'].str.contains(answer).empty:
        return (df[df['state'] == answer][['x', 'y']])
    return False

def update_title():
    screen.title(f"correct: {len(correct_answers)} / {total_states} - US States Guessing Game")

def display_answer(text, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(text, align="center")
    t.goto(0, 0)


def get_answer_from_text_box():
    return screen.textinput(title="Guessing States", prompt="Enter another guess")

def click_trigger(a, b):
    print(a,b)
    answer = get_answer_from_text_box().lower()
    if correct_answers.get(answer):
        return False
    coordinates = get_state_coordinates(answer)
    if not coordinates.empty:
        display_answer(answer, coordinates['x'].iloc[0], coordinates['y'].iloc[0])
        correct_answers[answer] = True
        update_title()

while len(correct_answers) < df.size:
    screen.onclick(click_trigger)
    turtle.mainloop()

