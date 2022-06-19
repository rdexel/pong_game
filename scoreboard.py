from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('White')
        self.goto(0, 250)
        
        self.l_score = 0
        self.r_score = 0

    def increase_score_l(self):
        self.l_score += 1

    def increase_score_r(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f'{self.l_score}', move=False, align='center', font=('Arial', 50, 'normal'))
        self.goto(100, 200)
        self.write(arg=f'{self.r_score}', move=False, align='center', font=('Arial', 50, 'normal'))

    def game_over(self):
        pass