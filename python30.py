from abc import ABC,abstractmethod
class something(ABC):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    @abstractmethod
    def area(self):
        pass
class rewrite(something):
    def area(self):
        result=0.5*self.base*self.height
        print('Area of triangle is: ',result)
obj1=rewrite(10,30)
obj1.area()