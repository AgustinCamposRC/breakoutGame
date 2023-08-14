from turtle import Turtle, Screen
from bricks import BreakManager
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

bricks_x_position = -250
bricks_y_position = 260
LIMIT_Y_AREA = 280

FONT = ('Righteous', 16, 'bold')

COLORS = ['#900C3F', '#C70039', '#F94C10', "#F8DE22"]
COLORS_POINTS = {
    '#900C3F':8, 
    '#C70039':6, 
    '#F94C10':4, 
    "#F8DE22":2
}


class BreakOut_Game(Turtle):

    def __init__(self):
        
        self.game_is_on = True
        self.lifes = 3

        self.screen = Screen()
        self.screen.setup(width=580, height=700)
        self.screen.bgcolor('black')
        self.screen.title("Breakout")
        self.screen.tracer(0)
        self.screen.listen()

        line = Turtle()
        line.goto(0, LIMIT_Y_AREA)
        line.shape('square')
        line.color('white')
        line.shapesize(stretch_wid=0.1,stretch_len=29)

        self.ball = Ball()
        self.bricks_manager = BreakManager()
        self.scoreboard = Scoreboard()
        self.scoreboard.lifes = self.lifes

        self.paddle = Paddle((0,-320))
        self.screen.onkey(self.paddle.go_right,'d')
        self.screen.onkey(self.paddle.go_left,'a')

        self.screen.onkey(self.paddle.go_right,'Right')
        self.screen.onkey(self.paddle.go_left,'Left')

        self.set_bricks_on_screen()

        self.message = Turtle()
        self.message.goto(0,0)
        self.message.hideturtle()
        self.message.color('white')
        self.message.write('Press Space to start the Game.',align='center',font=FONT)
        self.screen.update()
        self.screen.onkey(self.start_game, 'space')
        self.screen.mainloop()

    
    def set_bricks_on_screen(self):
        global bricks_x_position, bricks_y_position
        for levels in range(4):
            color_level = COLORS[levels]
            for _  in range(2):
                for _ in range(int(500/50)):
                    self.bricks_manager.create_break(
                        (bricks_x_position, bricks_y_position), 
                        color=color_level, 
                        points=COLORS_POINTS[color_level]
                    )
                    bricks_x_position+=55
                bricks_x_position = -250
                bricks_y_position -= 25


    def brick_collision(self):
        global bricks_x_position, bricks_y_position
        for brick in self.bricks_manager.all_break:
            if abs(brick.xcor() - self.ball.xcor()) < 51 and abs(brick.ycor() - self.ball.ycor()) < 22:
                self.ball.bounce_y()
                brick.hideturtle()
                brick.clear()
                self.scoreboard.add_points(brick.brickPoint)
                self.bricks_manager.all_break.remove(brick)


    def paddle_collision(self):
        distance_x = abs(self.paddle.xcor() - self.ball.xcor())
        distance_y =self.paddle.ycor() - self.ball.ycor()
        if (distance_x == 60 or distance_x < 60) and 20>=distance_y>=-20:
            self.ball.bounce_x()
        elif distance_x<61 and -20>distance_y>=-22:
            self.ball.bounce_y()


    def check_is_over(self):
           if self.ball.ycor() < -350:
                self.scoreboard.lifes -= 1
                self.scoreboard.update_score()
                if self.scoreboard.lifes == 0:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                self.ball.reset_position()
    

    def check_is_user_win(self):
        if self.bricks_manager.all_break == []:
             self.game_is_on = False

             self.scoreboard.win()

    def start_game(self):
        self.message.hideturtle()
        self.message.clear()
        self.gameplay()


    def gameplay(self):
        while self.game_is_on:

            self.screen.update()
            self.ball.move()
            time.sleep(0.001)
            self.paddle_collision()
            self.brick_collision() 

            if self.ball.xcor() == 275 or self.ball.xcor() == -285:
                self.ball.bounce_x()

            if self.ball.ycor() > LIMIT_Y_AREA -10:
                self.ball.bounce_y()

            self.check_is_over()
            self.check_is_user_win()

       
          
            
     
session = BreakOut_Game()