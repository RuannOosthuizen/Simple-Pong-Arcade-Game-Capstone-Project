# Imported Libraries:
from turtle import Turtle


# Defined Class:
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        '''This method updates the scoreboard.'''
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        '''This awards the left side player with a point.'''
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        '''This awards the right side player with a point.'''
        self.r_score += 1
        self.update_scoreboard()