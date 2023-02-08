from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.current_score}", move=False, 
        align="center", font=("Verdana", 20, "normal"))

    def add_point(self):
        self.current_score += 1
        self.print_score()