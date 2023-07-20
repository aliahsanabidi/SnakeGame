from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.relocate()

    def relocate(self):
        random_x = randint(-220, 220)
        random_y = randint(-220, 220)
        self.goto(random_x, random_y)