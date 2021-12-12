from random import randint

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
            and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True 
        else:
            return False 
            
class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return abs(self.)

rectanglex = Rectangle(Point(randint(0,9),randint(0,9)),Point(randint(10,19),randint(10,19)))

print("Rectangle Coordinates: ",rectanglex.lowleft.x,",",rectanglex.lowleft.y,"and",rectanglex.upright.x,",",rectanglex.upright.y)

user_point = Point(float(input("Guess X:")),float(input("Guess Y: ")))

print("your point was inside rectangle: ",
    user_point.falls_in_rectangle(rectanglex))