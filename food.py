from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        # inherit from the Turtle class
        super().__init__()
        self.shape("turtle")
        self.penup()
        # adjust the shape size of the food, width=default-size(20) * stretch_wid, length=default-size * stretch_len
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)