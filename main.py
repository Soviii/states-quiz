import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(700,600)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
stateList = data["state"].tolist()
userCorrectStates = []

userInput = screen.textinput(title="Guess the State", prompt="Enter either a state, \"exit\", \"history\", or \"help\"")
userInput = userInput.title()

attempts = 3
while attempts > 0:
    
    if userInput == "Exit":
        missing_states = pandas.DataFrame(stateList)
        missing_states.to_csv("states_to_learn.csv")
        break
    
    if userInput == "Help":
        userInput = screen.textinput(title="Guess the State", prompt="\"Exit\" ends the game and shows you what states you need to learn\n\"History\" shows what states you have entered\nEnter either a state or enter one of the previous options").title()

    elif userInput == "History":
        promptMessage = "You have answered these already: ", *userCorrectStates
        userInput = screen.textinput(title="Guess the State", prompt=promptMessage).title()

    elif userInput in stateList:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateCoords = data[data["state"] == userInput]
        t.goto(int(stateCoords["x"]), int(stateCoords["y"]))
        t.write(f"{userInput}", align="center", font=("Courier", 8, "normal"))
        screen.update()
        userCorrectStates.append(userInput)
        stateList.remove(userInput)
        if len(stateList) == 0:
            break
        userInput = screen.textinput(title="Guess the State", prompt="Nice job! Do you know another one? Enter it here.").title()

    else:
        userInput = screen.textinput(title="Guess the State", prompt=f"Dang! That's not a state, you have {attempts} left").title()
        attempts -= 1
        

if len(stateList) == 0:
    print("Good job")
    with open("states_to_learn.csv", "w") as file:
        file.write("You're a genius!")
else:
    print("Nice try")
    missing_states = pandas.DataFrame(stateList)
    missing_states.to_csv("states_to_learn.csv")
    

turtle.mainloop()


