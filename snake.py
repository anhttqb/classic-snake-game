from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_style()

    def create_snake(self):
        # Create a snake body including 3 squares in a line for the beginning
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def head_style(self):
        self.head.shape("circle")
        self.head.color("green yellow")
        self.head.shapesize(stretch_wid=1, stretch_len=1.5)

    def body_style(self):
        if len(self.segments) % 5 == 0:
            self.segments[len(self.segments) - 1].color("white")

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("dark red")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def body_extend(self):
        # Add a new segment to the snake by adding it into the last segment of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Use reverse loop to move the snake by moving the tail along with the body and the head
        for segment_num in range(len(self.segments) - 1, 0, -1):  # start=1, stop=0, step=-1
            #  Get the x and y positions of the next segment
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            #  Move the last segment to the positions of next segment
            self.segments[segment_num].goto(new_x, new_y)
        # move the head forward
        self.head.forward(MOVE_DISTANCE)

    # Create functions to be able to move the snake to 4 directions.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments: # Move the old snake out of the screen
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head_style()