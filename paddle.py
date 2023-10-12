import turtle as t


class Paddle(t.Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color('white')
        self.shape("square")  
        self.shapesize(stretch_wid=5,stretch_len=1)  
        self.penup()  
        self.pos = pos
        self.goto(350*pos, 0*pos) 
        self.dy = 40

    def moveUp(self):
        y = self.ycor()
        y += self.dy
        if y < 285:
            self.sety(y)
            
    def moveDown(self):
        y = self.ycor()
        y -= self.dy  
        if y > -280:
            self.sety(y)
 