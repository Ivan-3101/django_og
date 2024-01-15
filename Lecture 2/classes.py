# a class is basically a template for a type of object
# After defining a what a point is we can create 
# other points that store x and y values
# init is a method or function that is automatically gonna be called 
# everytime we try to creat a point
# https://youtu.be/EOLPQdVj5Ac?t=2641

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,8)
print(p.x)
print(p.y)
