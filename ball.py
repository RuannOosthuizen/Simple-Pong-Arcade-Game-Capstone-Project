# Imported Libraries:
from turtle import Turtle


# Defined Class:
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        '''Keeps the ball moving forward.'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''Bounces the ball off the top and buttom walls.'''
        self.y_move *= -1

    def bounce_x(self):
        '''Bounces the ball off from the paddles.'''
        self.x_move *= -1
        self.move_speed * 0.9

    def reset_position(self):
        '''This resets the balls position to the beginning.'''
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()