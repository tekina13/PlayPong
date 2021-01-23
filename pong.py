import turtle
import winsound
wn= turtle.Screen()
wn.title("Pong by Aniket")
wn.bgcolor("indigo")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

#Paddle A
paddle_A= turtle.Turtle()
paddle_A.speed(2)
paddle_A.shape("square")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.color("Black")
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B= turtle.Turtle()
paddle_B.speed(2)
paddle_B.shape("square")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.color("Black")
paddle_B.penup()
paddle_B.goto(350,0)
#Ball
Ball=turtle.Turtle()
Ball.speed(2)
Ball.shape("circle")
Ball.color("Yellow")
Ball.penup()
Ball.goto(0,0)

#pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0", align="center",font=("Arial",20,"normal"),)

Ball.dx=0.5
Ball.dy=0.5
#Paddle_A_up
def paddle_A_up():
    y=paddle_A.ycor()
    y+=20
    paddle_A.sety(y)
def paddle_A_down():
    y=paddle_A.ycor()
    y-=20
    paddle_A.sety(y)
def paddle_B_up():
    y=paddle_B.ycor()
    y+=20
    paddle_B.sety(y)
def paddle_B_down():
    y=paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")

# Main Game
while True:
    wn.update()
    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("poing.wav", winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("poing.wav", winsound.SND_ASYNC)
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a , score_b), align="center", font=("Arial", 20, "normal"))
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b +=1
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Arial", 20, "normal"))

    #paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_B.ycor() + 40 and Ball.ycor() > paddle_B.ycor() - 50):
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("bat.wav", winsound.SND_ASYNC)
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_A.ycor() + 40 and Ball.ycor() > paddle_A.ycor() - 50):
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound("bat.wav", winsound.SND_ASYNC)