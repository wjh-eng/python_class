
# class Dog:  # 狗
#     def jiaosheng(self):
#         print("汪，汪，汪")
#
#
# class Immortal: # 神仙
#     def huifei(self):
#         print("我要飞的更高")
#
#
# # 哮天犬这个子类 继承了Dog类和Immortal类
# class xiaotianquan(Dog, Immortal):
#     pass
#
#
# aaa = xiaotianquan()
#
# aaa.jiaosheng()
# aaa.huifei()


class Base:  #  源码
    def play(self):
        print("我是你祖宗")


class A(Base):  # 自己的代码
    def play(self):
        super().play()
        print("我是你祖宗的儿子")


class B(Base):
    def play(self):
        print("我是你祖宗的女儿")


class C(A, B):
    pass

c= C()
c.play()

print(C.mro())
