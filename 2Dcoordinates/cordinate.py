class Point:

    def __init__(self,x,y):

        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '({},{})'.format(self.x_cod,self.y_cod)

    def distance(self,other):

        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    def distance_from_origin(self):
        # return ((self.x_cod**2 + self.y_cod**2)**0.5) simple way to write the code of logic
        return self.distance(Point(10,20))

p1 = Point(10,20)

p2 = Point(10,0)

print(p1.distance(p2))


class Line:


    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c



    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.a,self.b,self.c)


    def point_on_line(line,point):
        if line.a*point.x_cod + line.b*point.y_cod +line.c == 0:
            return "lies on the line "

        else:
            return "does not lie on line"


         



l1 = Line(2,6,3)
p1 = Point(8,2)

print(l1)
print(p1)

print(l1.point_on_line(p1))









