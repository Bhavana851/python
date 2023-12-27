class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.x = 12
point1.y = 13
print(point1.x)
print(point1.y)
point1.draw()

point2 = Point()
point2.x = 40
point2.y = 52
print(point2.y)
print(point2.x)
point2.move()

