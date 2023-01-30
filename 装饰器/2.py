"""
登录注册
验证用户名的功能
"""

"""
春风十里不如你,三里桃花不及卿

不改变原有函数代码和调用的基础上，给函数增加新的功能
"""


# g = girl()
# print(g)

# def modifty(func):
#     def wrapper():
#         print("正在被装饰---")
#         result = func()
#         print(result)
#         print("已经装饰完成了---")
#
#     return wrapper
#
# @modifty  #只会影响一行  语法糖  @装饰器的名字
# def girl():
#     return "春风十里不如你"
#
# g = girl()

# class Rectangle:
#     def __init__(self):
#         pass
#
#     @property # 被装饰的方法可以像访问属性一样 进行使用
#     def area(self):
#         return "我真的被property装饰了"
#
#     @classmethod  # 类装饰器 传递的是类本身 直接变成类方法
#     def func(cls):
#         print(cls)
#         return "我被classmethod装饰了"
#
#     @staticmethod # 静态装饰器  和class断开关系  不加self
#     def tongyao():
#         return "我也被装饰了"
#
# a = Rectangle()
# # print(a.area)
# # print(a.func())
# # print(a.tongyao())
# # print(Rectangle.tongyao())
# print(Rectangle.func())



# class TestClass:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("类---call---")
#         return self.func()
# @TestClass
# def func_test():
#     print("这是一个测试函数")
#
# func_test()
#
# isinstance()


# import time
#
# a = time.time() # 开始时间
# for i in range(10000000):
#     type("hello")  # 程序执行
# b = time.time() # 结束时间
#
# print(b-a)