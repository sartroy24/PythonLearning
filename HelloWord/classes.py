class Point:
    def move(self):
        print("move")
        
    
    def draw(self):
        print("draw")
        
        
point1 = Point()
point1.draw()
point1.move()

point1.x = 20
point1.y = 30
print(point1.x, point1.y )