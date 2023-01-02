import random

def guess_number():
    b = random.randint(1, 100)
    while True:
        try:
            a = input("请输入猜的数字： ")
            if int(a) > int(b):
                print("你猜的太大了")
            elif int(a) < (b):
                print("你猜的太小了")
            elif int(a) == int(b):
                print("你猜对了")
            else:
                break
        except ValueError:
            break


def cal_sum(n=100):
    sum = 0
    for i in range(1,n+1,2):
        sum = sum + i
    print(sum)

def draw_tri():
    n = int(input("输入值： "))
    for i in range(1,n):
        print(' '*(n-1-i), '*'*(2*i-1))

draw_tri()
cal_sum(102)
guess_number()


#enumerate()输入可迭代对象，返回索引和对应元素
#enumerate(sequence, [start=0])   start 下标开始位置
li = [233,3454,'dfds',(2,3445,6)]
for i, element in enumerate(li):
    print(i, element)


#eval()输入表达式，返回表达式计算结果
res1 = eval('3*4')
res2 = eval('pow(3,5)')
print(res1,res2)


#filter()输入判断函数和可迭代对象，返回迭代器对象
def is_odd(n):
    return n % 2 == 1
newlist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(newlist)


#map()输入函数对象和可迭代对象，输出每个元素被函数操作后的迭代器
def square(x) :         # 计算平方数
    return x ** 2
print(list(map(square, [1,2,3,4,5])))
li = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(li))

#zip()输入一个或多个迭代器，返回对应元素元组组成的列表
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
print(list(zipped))
a1,b1 = zip(*zip(a,b))
print(list(a1),list(b1))