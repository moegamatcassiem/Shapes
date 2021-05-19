class Shapes:
    def __init__(self, name, side):
        self.name=name
        self.side=side
    def Area(self):
        print("I am a :" + self.name + "\n"+
              "I have " + self.side + "sides")
obj_shape=Shapes("shape", "so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length=len1
        self.width=wid1
    def Area(self):
        result=self.length * self.width
        return result
obj_book=Rectangle(10, 7)
obj_screen=Rectangle(5, 7)
print("The area of a book is" + str(obj_book.Area()))
print("The area of a screen is" + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self, rad1, rad2, pie):
        self.radius=rad1
        self.radius2=rad2
        self.pie=3.14
    def Area(self):
        result=self.radius * self.radius2 * self.pie
        return result
obj_plate=Circle(5, 5, 3.14)
print("The area of a plate is" + str(obj_plate.Area()))

class Triangle(Shapes):
    def __init__(self, b, hei1):
        self.base=b
        self.height=hei1
    def Area(self):
        result=self.base * self.height
        return result
obj_sign=Triangle(4, 10)
print("The area of a sign is" + str(obj_sign.Area()))