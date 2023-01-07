"""
什么是类！ class
为什么要学类！  面向对象的编程语言
封装  继承 （多态）（鸭子类型）
不学有啥影响？
"""
# import requests
# import random

# random.randint()
# random.choice()
# Person
# 属性：名字，身高，性别，年龄
# 方法：会工作，会走路，会唱歌，会吃饭

# class Person:  # class 类名：
#     name='tongyao'   # 属性
#     def smile(self):  #  方法
#         print('smiling')
"""
类和对象的关系
 1 具有相同属性和功能的一类事物  （抽象的）
 2 一个类可以找到多个对象
 
对象：
 1.类的具体表现
 2.对象是看得见摸得着，可以直接使用的
"""

class MyPerson(object):
    def __init__(self,name,age): #  初始化
        self.name = name
        self.age = age

    def smile(self):  # 方法
        print('smiling')

    def my_self(self): # self就等于实例本身 = haha
        print('我叫{}，我岁{}了'.format(self.name,self.age))


tongyao = MyPerson('tongyao','18')
tongyao.my_self()





# class Person:
#     def __init__(self):
#         print("我是构造方法")
#
#     def __del__(self):
#         print("我被销毁了")
#
#
#
#
# xm = Person()
# while True:
#     print(xm)

# class A:
#     def __str__(self): # 魔法方法
#         return "hello"
#
# obj = A()  # 类的实例化
# print(obj)

# print(obj)  #  __str__




class A:
    pass



