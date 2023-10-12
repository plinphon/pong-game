from ball import Ball
from paddle import Paddle
import turtle
from scoreboard import Scoreboard
import time

wn = turtle.Screen()
wn.listen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
ball = Ball()
paddler = Paddle(1)
paddlel = Paddle(-1)
scoreboard = Scoreboard()
scoreboard.writer()

def quit():
    wn.bye()

wn.onkey(fun= paddler.moveUp,key='Up')
wn.onkey(fun= paddler.moveDown,key='Down')
wn.onkey(fun= paddlel.moveUp,key='w')
wn.onkey(fun= paddlel.moveDown,key='s')
wn.onkey(fun= quit,key='q')

while True:
   
    wn.update()
    ball.move()

    if ball.ycor() > 290:
        ball.bounce_y()

    if ball.ycor() < -290:
        ball.bounce_y()
    
    if ball.ycor() < paddler.ycor()+50 and ball.ycor() > paddler.ycor()-50 and ball.xcor() == paddler.xcor()-10:
        ball.bounce_x()

    if ball.ycor() < paddlel.ycor()+50 and ball.ycor() > paddlel.ycor()-50 and ball.xcor() == paddlel.xcor()+10:
        ball.bounce_x()
    
    if ball.xcor() < paddler.xcor()+10 and ball.xcor() > paddler.xcor()-10:
        if ball.ycor() == paddler.ycor()-50 or ball.ycor() == paddler.ycor()+50:
           ball.bounce_y()

    if ball.xcor() < paddlel.xcor()+10 and ball.xcor() > paddlel.xcor()-10:
        if ball.ycor() == paddlel.ycor()-50 or ball.ycor() == paddlel.ycor()+50:
           ball.bounce_y()

    if ball.xcor() > 390:
        scoreboard.left +=1
        scoreboard.writer()
        ball.reset_ball()
        
    if ball.xcor() < -390:
        scoreboard.right +=1
        scoreboard.writer()
        ball.reset_ball()

        



    

