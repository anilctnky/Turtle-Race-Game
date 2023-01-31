from turtle import Turtle, Screen
turn_angle = 0
import random
is_race_on = False

def create_turtle(color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    return new_turtle

# def move_forward():
#     muf.forward(20)
#
#
# def move_backward():
#     muf.backward(20)
#
#
# def turn_left():
#     global turn_angle
#     turn_angle += 22.5
#     muf.setheading(turn_angle)
#
#
# def turn_right():
#     global turn_angle
#     turn_angle -= 22.5
#     muf.setheading(turn_angle)
#
#
# def clear_screen():
#     muf.clear()
#     muf.penup()
#     muf.home()
#     muf.pendown()
#
#

screen = Screen()
screen.listen()
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -66, -33, 0, 33, 66]
racer_turtles = []

for index in range(0, 6):
    muf = create_turtle(colors[index])
    muf.goto(x=-230, y=y_positions[index])
    racer_turtles.append(muf)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in racer_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            current_color = turtle.pencolor()
            if current_color == user_bet:
                print(f"You have won the race. The winner color is {user_bet}")
            else:
                print(f"You have lost the race. The winner color is {current_color}")
        rand_distance = random.randint(5, 20)
        turtle.forward(rand_distance)


screen.exitonclick()
