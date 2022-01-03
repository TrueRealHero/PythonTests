import turtle

window = turtle.Screen()
window.title('PingPong')
window.bgcolor('white')
window.setup(width=600, height=400)
window.tracer(0)


class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape('square')
        self.player.color('black')
        self.player.shapesize(stretch_wid=4, stretch_len=1)
        self.player.penup()


class PlayerOne(Player):
    def __init__(self):
        super().__init__()
        self.player.goto(-270,0)
    
    def move_up(self):
        self.y = self.player.ycor()
        self.y += 20
        self.player.sety(self.y)

    def move_down(self):
        self.y = self.player.ycor()
        self.y -= 20
        self.player.sety(self.y)


class PlayerTwo(Player):
    def __init__(self):
        super().__init__()
        self.player.goto(270,0)

    def move_up(self):
        self.y = self.player.ycor()
        self.y += 20
        self.player.sety(self.y)

    def move_down(self):
        self.y = self.player.ycor()
        self.y -= 20
        self.player.sety(self.y)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape('square')
        self.ball.color('black')
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = 1
        self.ball.dy = 1

    def move(self):
        if self.ball.ycor() > 190:
            self.ball.sety(190)
            self.ball.dy *= -1

        if self.ball.ycor() < -180:
            self.ball.sety(-180)
            self.ball.dy *= -1

        if self.ball.xcor() > 270:
            self.ball.goto(0,0)
            self.ball.dx *= -1

        if self.ball.xcor() < -270:
            self.ball.goto(0,0)
            self.ball.dx *= -1

        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def collision(self):
        if self.ball.xcor() > 250 and self.ball.ycor() < player_two.player.ycor() + 40 and self.ball.ycor() > player_two.player.ycor() - 40:
            self.ball.setx(250)
            self.ball.dx *= -1
            
        if self.ball.xcor() < -250 and self.ball.ycor() < player_one.player.ycor() + 40 and self.ball.ycor() > player_one.player.ycor() - 40:
            self.ball.setx(-250)
            self.ball.dx *= -1


class Table:
    def __init__(self):
        self.table = turtle.Turtle()
        self.table.speed(0)
        self.table.color("black")
        self.table.penup()
        self.table.hideturtle()
        self.table.goto(0, 160)
        self.table.one = 0
        self.table.two = 0

    def scoring(self):
        if ball.ball.xcor() > 270:
            self.table.clear()
            self.table.one += 1

        if ball.ball.xcor() < -270:
            self.table.clear()
            self.table.two += 1

        self.table.write("{} : {}".format(self.table.one, self.table.two), align="center", font=("Courier", 20, "normal"))



# Class copies
player_one = PlayerOne()
player_two = PlayerTwo()
ball = Ball()
table = Table()


#Keyboard bindings
window.listen()
window.onkeypress(player_one.move_up, 'w')
window.onkeypress(player_one.move_down, 's')
window.onkeypress(player_two.move_up, 'Up')
window.onkeypress(player_two.move_down, 'Down')


#Game loop
while True:
    # Ball bounce and collision
    ball.move()
    ball.collision()

    # Table updating
    table.scoring()

    # Window loop
    window.update()