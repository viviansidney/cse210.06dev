class Snake:
    def __init__(self):
        self.headposition = (20, 0)
        self.body = [Square (-20, 0, Square(0, 0), Square(20, 0)]
        self.nextX = 1
        self.nextY = 0
        self.crashed = False
        self.nextposition = [self.headposition[0] + 20*self.nextX, 
                             self.headposition[1] + 20*self.nextY]
        
    def moveOneStep(self):
        if Square(self.nextposition, self.nextposition[0],
                  self.nextposition[1] not in self.body):
            self.body.append(Square(self.nextposition[0], self.nextposition[1]))
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1]
                 .x, self.body[-1]
            self.nextposition = [self.headposition[0] + 20*self.nextX,
                                 self.headposition[1] + 20*self.nextY]
        else:
            self.crashed = True
    
    def moveup(self):
        self.nextX = 0
        self.nextY = 1        
        
    def moveleft(self):
        self.nextX = -1
        self.nextY = 0
        
    def moveright(self):
        self.next = 1
        
    def movedown(self):
        self.nextX = 0
        self.nextY = -1
        
    def eatFood(self):
        self.body.append(Square(self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].y
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                self.headposition[1] + 20*self.nextY]
        
    def drawself(self, turtle):
        for segment in self.body:
            segment.drawself(turtle)