from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color, points):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(position)
        self.brickPoint = points

class BreakManager:

    def __init__(self):
        self.all_break = []

    def create_break(self, position: tuple, color, points):
        newBreak = Brick(position, color, points)
        
        self.all_break.append(newBreak)
