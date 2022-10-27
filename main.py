    
    
def snakeup(self):
       print("goin up")
       if not self.commandpending:
        self.snake.moveup()
        self.commandpending = True
def snakedown(self):
       print("going down")
       if not self.commandpending:
        self.snake.movedown()
        self.commandpending = True
        
def snakeleft(self):
       print("going left")
       if not self.commandpending:
        self.snake.moveleft()
        self.commandpending = True
        
def snakeright(self):
       print("going right")
       if not self.commandpending:
        self.snake.moveright()
        self.commandpending = True
        
game = Game ()
game.nextFrame()
print("game over")

game.screen.mainloop()
        

    
    
           
