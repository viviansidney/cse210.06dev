import random
import turtle
import time

class Square:
    def __init__(self, x, y):
       self.x = x
       self.y = y
       
    def drawself(self, turtle):
        turtle.goto(self.x - 9, self.y -9)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()
        
        