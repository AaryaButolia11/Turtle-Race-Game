from turtle import Turtle,Screen
import random
screen=Screen()

#allows to set width & height of a screen using .setup(<width>,<height>) method
screen.setup(width=500,height=400)

"""
turtle.textinput(<title>,<prompt>)
title-string
prompt-string
Pop up a dialog window for input of a string. Parameter title is the title of the dialog window, 
prompt is a text mostly describing what information to input. Return the string input. If the dialog is canceled, return None.
"""
is_race_on=False
user_bet=screen.textinput(title="Make your bet!",prompt="Which turtle is going to win the race? Enter a color (VIBGYOR): ")

y_positions=[-70,-40,-10,20,50,80]
colors=["red","orange","yellow","green","blue","purple"]
all_turtle=[]
for turtle_index in range(0,6):

    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    #the .goto(x=,y=) takes the turtle to desired x & y coordinates
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)
if user_bet :
    is_race_on=True
while is_race_on:
    for turtle in all_turtle: 
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=(turtle.pencolor())
            if winning_color == user_bet:
                print("you have won!! The {winning_color} is the winner!")
            else:
                print("you have lost!! The {winning_color} is the winner! ")

        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
    
screen.exitonclick()