class Point:
        def move(self):
            print('hi move')


        def draw(self):
            print('hi draw')


point1 = Point()
print('Start ')
point1.draw()
point1.move()
print('finish')
#---------------------
point2 = Point()
point2.x = 102342354
point2.y = 20
print(point2.x)
point2.draw()
#print(point1.x +'hfsehfkjn') we will get error here for not creating a arguments for point2 object

#---------------------


