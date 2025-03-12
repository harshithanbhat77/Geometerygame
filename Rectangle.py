from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        return (min(rect.point1.x, rect.point2.x) <= self.x <= max(rect.point1.x, rect.point2.x)) and \
               (min(rect.point1.y, rect.point2.y) <= self.y <= max(rect.point1.y, rect.point2.y))


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y))


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        if not isinstance(canvas, turtle.Turtle):
            raise TypeError("canvas must be an instance of turtle.Turtle")

        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(abs(self.point2.x - self.point1.x))
        canvas.left(90)
        canvas.forward(abs(self.point2.y - self.point1.y))
        canvas.left(90)
        canvas.forward(abs(self.point2.x - self.point1.x))
        canvas.left(90)
        canvas.forward(abs(self.point2.y - self.point1.y))
        canvas.left(90)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='Yellow'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object
rect = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates:", rect.point1.x, ",", rect.point1.y, "and", rect.point2.x, ",", rect.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle:", user_point.falls_in_rectangle(rect))
print("Your area was off by:", abs(rect.area() - user_area))

# Draw the shapes
myturtle = turtle.Turtle()
rect.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
