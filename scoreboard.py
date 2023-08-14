from turtle import Turtle

FONT = ('Righteous', 16, 'bold')
START_POSITION = (-270,320)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(START_POSITION)
        self.points = 0
        self.Lifes = 0
        self.update_score()
    

    def add_points(self, points):
        self.points += points
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(START_POSITION)
        self.write(f'Brick Points: {self.points}',align='left',font=FONT)
        self.goto(-230, 290)
        self.write(f'Lifes: {self.Lifes}',align='center',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write('Game Over',align='center',font=FONT)


    def win(self):
        self.goto(0,0)
        self.color('green')
        self.write('You Win!!!',align='center',font=FONT)
