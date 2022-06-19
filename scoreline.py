from turtle import Turtle


class ScoreLine(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 300)
        self.forward(600)
