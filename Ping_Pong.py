import turtle
from turtle import Turtle

w=turtle.Screen()
w.title("Pong by @varunsai09")
w.bgcolor("black")
w.setup(width=800,height=600)
w.tracer(0) #stop s from updating and we can speed up
#score
score_a=0
score_b=0


#paddle a
paddle_a= turtle.Turtle()
paddle_a.speed(0)  #speed of animation i.e to max level
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    #default 20 pixels both
paddle_a.penup()
paddle_a.goto(-350,0)



#paddle b
paddle_b= turtle.Turtle()
paddle_b.speed(0)  #speed of animation i.e to max level
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #default 20 pixels both
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball: Turtle= turtle.Turtle()
ball.speed(0)  #speed of animation i.e to max level
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-0.1
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

def paddle_a_up():
    y= paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)
    pen.write("Player A: Player B:0", align="centre", font=("Courier",24,"normal"))

def paddle_a_down():
    y= paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)

#keyboard binding
w.listen()
w.onkeypress(paddle_a_up,"w")
w.onkeypress(paddle_a_down,"s")
w.onkeypress(paddle_b_up,"Up")
w.onkeypress(paddle_b_down,"Down")


#main game loop
while True:
    w.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety (-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
         ball.goto(0,0)
         ball.dx *= -1
         score_a+=1
         pen.clear()
         pen.write("Player A:{} Player B:{}".format(score_a , score_b), align="centre", font=("Courier",24,"normal"))

    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), align="centre", font=("Courier",24,"normal"))
    #paddle and ball collisions

    if (ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
