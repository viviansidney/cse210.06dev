import random
import turtle


class Food:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.state = "ON"
        
    def changelocation(self):
        self.x = random.randint(o, 20) * 20 - 200
        self.y = random.randint(0, 20) * 20 - 200
        
    def drawself(self, turtle):
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y - 9)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()
            
    def changestate(self):
        self.state + "OFF" 
        if self.state == "ON" 
        else: "ON"