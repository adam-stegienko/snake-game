from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"SCORE: {self.current_score}, HIGH SCORE: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def add_point(self):
        self.current_score += 1
        self.print_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGN, font=FONT)

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.print_score()