class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        result=0.5*self.base*self.height
        print('The area of the triangle is:', result)
t1=triangle(10,5)
t1.area()
t2=triangle(100,300)
t2.area()