# Imported Libraries:
from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# The screen setup:
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Creating object:
r_paddle = Paddle((350, 0)) # right paddle
l_paddle = Paddle((-350, 0)) # left paddle
ball = Ball()
screen.listen()
scoreboard = Scoreboard()


# Right paddle controls:
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left paddle controls:
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# Refreshes the screen:
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Keeping the ball moving:
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


# Closes the window on a click:
screen.exitonclick()
