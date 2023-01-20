"""
魔法方法  __方法名__   左右各两个下换线
"""

# class A:
#     def __init__(self,num1):
#         self.num1 = num1
#
#     def __add__(self, other):
#         sum1 = self.num1 + other.num1  # other 另外一个实例
#         print(self.num1)
#         print(other.num1)
#         return '我重写了add方法：{}'.format(sum1)
#
# a = A(4)
# b = A(2)
# c = A(3)
#
# print(a + b)

# __sub__  x-y
# __iadd__(self, other)  x += y


# class  Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         res = self.length*self.width
#         return res
#
#     # 重写call方法
#     def __call__(self, *args, **kwargs):
#         # 随便返回什么都行
#         print("this is __call__")
#         # return "this is __call__"
#
#
# a = Rectangle(10, 1)  #38行这个过程叫做类的实例化   a 叫做 类的实例
# a()  # __call__ 方法 实现了 类的实例可以直接进行调用
#




# class A:
#     def  __init__(self,tong):
#         self.tong = tong
#
#     def __add__(self, other):
#         res = self.tong + other.tong
#         print(res)
#
#
# a = A("10")
# b = A("5")
#
# a + b

# class A:
#     def __call__(self, *args, **kwargs):
#         print(args)
#         return "我重写了call 方法"
# a = A()
print()



