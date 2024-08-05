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

wn.exitonclick()