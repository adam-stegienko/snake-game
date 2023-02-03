#!/bin/env python3

# Importing modules
import time
from snake import Snake
from turtle import Turtle, Screen

# Snake game nokia screen initial set-up
nokia_screen = Screen()
nokia_screen.setup(width=600, height=600)
nokia_screen.bgcolor("black")
nokia_screen.title("Nokia Snake Game")
nokia_screen.tracer(0)

# Snake initial set-up
snake = Snake()
nokia_screen.update()

# Game start - boolean
is_game_on = True
while is_game_on:
    nokia_screen.update()
    time.sleep(0.1)

    snake.move()






# Exit screen on click in the end of the program run
nokia_screen.exitonclick()