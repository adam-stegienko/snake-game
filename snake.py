from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [0, 0]

class Snake:
    def __init__(self):
        self.build_snake()

    def build_snake(self):
        self.all_elements = []
        for _ in range (0, 3):
            snake_element = Turtle()
            snake_element.penup()
            snake_element.shape("square")
            snake_element.color("white")
            snake_element.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
            self.all_elements.append(snake_element)
            STARTING_POSITION[0] -= MOVE_DISTANCE

    def body(self):
        return self.all_elements

    def move(self):
        snake_length = len(self.body())
        whole_snake = self.body()
        for block in range(snake_length -1, 0, -1):
            new_x = whole_snake[block - 1].xcor()
            new_y = whole_snake[block - 1].ycor()
            whole_snake[block].goto(x=new_x, y=new_y)
        whole_snake[0].forward(MOVE_DISTANCE)
