class Tree: 
    
    def __init__(self, turtle):
        self.turtle = turtle
        self.turtle.left(90)

    def createTree(self, size):
        if size < 5:
            self.turtle.forward(size)
            self.turtle.backward(size)
            return
        else:        
            self.turtle.forward(size/3)
            self.turtle.left(30)
            self.createTree(size*2/3)
            self.turtle.right(30)
            self.turtle.forward(size/6)
            self.turtle.right(25)
            self.createTree(size/2)
            self.turtle.left(25)
            self.turtle.forward(size/3)
            self.turtle.right(25)
            self.createTree(size/2)
            self.turtle.left(25)
            self.turtle.forward(size/6)
            self.turtle.backward(size)
