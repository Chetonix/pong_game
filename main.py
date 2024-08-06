from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

wn = Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Pong")
wn.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()


wn.listen()
wn.onkey(r_paddle.go_up, "Up")
wn.onkey(r_paddle.go_down, "Down")

wn.onkey(l_paddle.go_up, "w")
wn.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    wn.update()
    ball.move()

    #detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < - 320):
        ball.bounce_x()

wn.exitonclick()