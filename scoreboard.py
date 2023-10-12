import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.left = 0
        self.right = 0
        self.hideturtle()
        self.penup() 
        self.goto(0, 200)  
        self.pendown() 
    
    def writer(self):
        self.clear()
        self.write(f'{self.left} : {self.right}',
                   align="center",
                   font = ('Arial', 50, 'normal'))