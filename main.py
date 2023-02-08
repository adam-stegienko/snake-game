#!/bin/env python3

# Importing modules
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

# Snake game nokia screen initial set-up
nokia_screen = Screen()
nokia_screen.setup(width=600, height=600)
nokia_screen.bgcolor("black")
nokia_screen.title("Nokia Snake Game")
nokia_screen.tracer(0)

# Snake and food initial set-up
snake = Snake()
food = Food()
scoreboard = Scoreboard()

nokia_screen.listen()
nokia_screen.onkey(snake.up, "Up")
nokia_screen.onkey(snake.down, "Down")
nokia_screen.onkey(snake.left, "Left")
nokia_screen.onkey(snake.right, "Right")

# Game start - boolean
is_game_on = True
while is_game_on:
    nokia_screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_point()
        food.generate()






# Exit screen on click in the end of the program run
nokia_screen.exitonclick()