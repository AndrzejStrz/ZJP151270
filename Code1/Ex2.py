import random
class Coin:
    def __init__(self):
        self.side = random.choice(['head','tail'])
        
    def throw(self):
        self.side = random.choice(['head','tail'])
    
    def show_side(self):
        print(self.side)

c1 = Coin()
c1.show_side()
c1.throw()
c1.show_side()