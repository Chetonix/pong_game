from turtle import Turtle, Screen
from paddle import Paddle

wn = Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Pong")
wn.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))



wn.listen()
wn.onkey(r_paddle.go_up, "Up")
wn.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    wn.update()

wn.exitonclick()