from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.generate()

    def generate(self):
        random_coordinates = (randint(-280, 280), randint(-280, 280))
        self.goto(random_coordinates)