import turtle
import pandas

screen = turtle.Screen() 
screen.title("U.S State Name Guessing")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
game_is_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_list = []
missed_list = []
while len(guessed_list) < 50:
    answer = screen.textinput(title=f"{len(guessed_list)} / 50 States correct", prompt="Enter the name of the state ").title()
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    # if answer == "Exit":
    #     for state in all_states:
    #         if state not in guessed_list:
    #             missed_list.append(state)
    #     new_data = pandas.DataFrame(missed_list)
    #     new_data.to_csv("state_to_learn.csv")
    #     break

    if answer == "Exit":
        missed_list = [state for state in all_states if state not in guessed_list]
        pandas.DataFrame(missed_list).to_csv("state_to_learn2.csv")
        break
        
    if answer in all_states:
        if answer not in guessed_list:
            guessed_list.append(answer)
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)

print(missed_list)
turtle.bye()
