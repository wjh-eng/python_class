
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def cal_area(self):
        return self.length * self.width
    def __call__(self):
        print("面积为{}".format(self.cal_area()))

rectangle = Rectangle(60,40)
area = rectangle.cal_area()
print(area)
class Square(Rectangle):
    def __init__(self,bianchang):
        super().__init__(bianchang,bianchang)
a = Square(100)
a()
