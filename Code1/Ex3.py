class Rectangle:
    def __init__(self,a: float, b:float):
        self.a = a
        self.b = b


    def surface_area(self) -> float:
        return self.a*self.b

def ex3fun(rectangle):
    print('a= ',rectangle.a)
    print('b= ',rectangle.b)
    print('surfece area= ',rectangle.surface_area())
    

pr1 = Rectangle(1,2)
pr2 = Rectangle(2,5.3)
prlist = [pr1,pr2]

#e)
for x in prlist:
    print(x.surface_area())

#f)
ex3fun(pr1)
ex3fun(pr2)