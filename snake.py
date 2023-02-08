from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [0, 0]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_elements = []
        self.starting_elements = 3
        self.build_snake(elements=self.starting_elements)
        self.head = self.all_elements[0]

    def build_snake(self, elements):
        for _ in range(elements):
            self.extend_snake()

    def extend_snake(self):
        snake_element = Turtle()
        snake_element.penup()
        snake_element.shape("square")
        snake_element.color("white")
        snake_element.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
        self.all_elements.append(snake_element)
        STARTING_POSITION[0] = (self.all_elements[-1].xcor() - MOVE_DISTANCE)

    def body(self):
        return self.all_elements

    def move(self):
        snake_length = len(self.all_elements)
        for block in range(snake_length -1, 0, -1):
            new_x = self.all_elements[block - 1].xcor()
            new_y = self.all_elements[block - 1].ycor()
            self.all_elements[block].goto(x=new_x, y=new_y)
        self.all_elements[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)