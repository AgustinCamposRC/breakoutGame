from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.shape('square')
        self.color('#EC8856')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(position)

    def go_right(self):
        if self.xcor() < 210:
            new_x = self.xcor() + 30
            self.goto((new_x,self.ycor()))
    
    def go_left(self):
        if self.xcor() > -220:
            new_x = self.xcor() - 30
            self.goto((new_x,self.ycor()))
    