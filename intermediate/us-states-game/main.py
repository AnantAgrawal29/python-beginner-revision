import turtle
import pandas

def createState(state,x,y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.write(state, font=('Courier', 8, 'normal'))

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(f'{len(guessed_states)}/50 States Correct', 'What\'s another states name?').capitalize()
    if guess=='Exit':
        missed_states = [state for state in states if state not in guessed_states]  # List Comprehension              
        pandas.Series(missed_states).to_csv('Missed States.csv')
        break
    if guess in states and guess not in guessed_states:
        guessed_states.append(guess)
        createState(guess, data[data.state == guess].x.item(), data[data.state == guess].y.item())