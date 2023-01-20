class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        res = self.length*self.width
        return res


class Square(Rectangle):
    def __init__(self, length, width, height ):
        self.height = height
        if length == width:
            Rectangle.__init__(self, length, width)  # 第一种方法
            # super().__init__(length, width) # 第二种方法
        # else:
        #     self.length = length
        #     self.width = width
        #     # print("边长不相等，所以这不是一个正方形")

    def tiji(self):
        res = self.length*self.width*self.height
        return res



a = Square(10, 10)
print(a.area())



