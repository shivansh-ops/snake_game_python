from turtle import Turtle
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(a=-280, b=280)
        random_y = randint(a=-280, b=280)
        self.goto(random_x, random_y)
