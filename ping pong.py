import os
import turtle


window = turtle.Screen()
window.title('PingPong')
window.bgcolor('white')
window.setup(width=600, height=400)
window.tracer(0)

player_one = turtle.Turtle()
player_one.speed(0)
player_one.shape('square')
player_one.color('black')
player_one.shapesize(stretch_wid=4, stretch_len=1)
player_one.penup()
player_one.goto(-270,0)

player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape('square')
player_two.color('black')
player_two.shapesize(stretch_wid=4, stretch_len=1)
player_two.penup()
player_two.goto(270,0)

def move_up1():
    y = player_one.ycor()
    y += 20
    player_one.sety(y)

def move_down1():
    y = player_one.ycor()
    y -= 20
    player_one.sety(y)

def move_up2():
    y = player_two.ycor()
    y += 20
    player_two.sety(y)

def move_down2():
    y = player_two.ycor()
    y -= 20
    player_two.sety(y)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

table = turtle.Turtle()
table.speed(0)
table.color("black")
table.penup()
table.hideturtle()
table.goto(0, 160)

window.listen()
window.onkeypress(move_up1,'w')
window.onkeypress(move_down1,'s')
window.onkeypress(move_up2,'Up')
window.onkeypress(move_down2,'Down')

one = 0
two = 0
table.write("{} : {}".format(one, two), align="center", font=("Courier", 20, "normal"))

#Game loop
while True:
    # Ball bounce from bars
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -180:
        ball.sety(-180)
        ball.dy *= -1

    if ball.xcor() > 270:
        ball.goto(0,0)
        ball.dx *= -1
        one += 1
        table.clear()
        table.write("{} : {}".format(one, two), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -270:
        ball.goto(0,0)
        ball.dx *= -1
        two += 1
        table.clear()
        table.write("{} : {}".format(one, two), align="center", font=("Courier", 20, "normal"))

    # Collision
    if ball.xcor() > 250 and ball.ycor() < player_two.ycor() + 40 and ball.ycor() > player_two.ycor() - 40:
        ball.setx(250)
        ball.dx *= -1

    if ball.xcor() < -250 and ball.ycor() < player_one.ycor() + 40 and ball.ycor() > player_one.ycor() - 40:
        ball.setx(-250)
        ball.dx *= -1

    # Window loop
    window.update()