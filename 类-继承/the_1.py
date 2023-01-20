"""
长方形类
有一个计算面积的方法
"""

class  Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        res = self.length*self.width
        return res


a = Rectangle(10, 3)
b = Rectangle(11, 3)
print(a.area())
print(b.area())

# ------------------
# def data():
#     return "hello world"
#
# data()




