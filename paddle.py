# Imported Libraries:
from turtle import Turtle


# Defined Class:
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        '''Moves paddle upwards.'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''Moves paddle downwards.'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)