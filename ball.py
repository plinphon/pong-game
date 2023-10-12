import turtle as t


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape("circle")  
        self.penup()  
        self.goto(0, 0) 
        self.dx = 2 
        self.dy = -2

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1
    
    def reset_ball(self):
        self.goto(0, 0)
        

