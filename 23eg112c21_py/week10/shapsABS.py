from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def area(self, r):
        print("Area of circle is: ", 3.14*r*r)
    def perimeter(self, r):
        print("Perimeter of circle is: ", 2*3.14*r)
class rectangle(shape):
    def area(self, l, b):
        print("Area of rectangle is: ", l*b)
    def perimeter(self, l, b):
        print("Perimeter of rectangle is: ", 2*(l+b))
class triangle(shape):
    def area(self, b, h):
        print("Area of triangle is: ", 0.5*b*h)
    def perimeter(self, a, b, c):
        print("Perimeter of triangle is: ", a+b+c)
c = circle()
c.area(5)
c.perimeter(5)
r = rectangle()
r.area(5, 6)
r.perimeter(5, 6)
t = triangle()
t.area(5, 6)
t.perimeter(3, 4, 5)
