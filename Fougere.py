class Fern: 
    
    def __init__(self, turtle):
        self.turtle = turtle
        turtle.left(90)

    def createFern(self, size, sign):
        if size < 1:
            return
        else:
            self.turtle.forward(size)
            self.turtle.right(70*sign)

            self.createFern(size*0.5, -1*sign)

            self.turtle.left(70*sign)
            self.turtle.forward(size)
            self.turtle.left(70*sign)

            self.createFern(size*0.5, sign)

            self.turtle.right(70*sign)
            self.turtle.right(7*sign)

            self.createFern(size-1, sign)

            self.turtle.left(7*sign)
            self.turtle.backward(size*2)
