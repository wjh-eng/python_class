'''
enumerate
eval
map
zip
'''

def func():
    print("hello")
    return 'hello'
func()
print(func())

li = ['ad','wef','ewf']
e = enumerate(li)
print(list(e))

a = '1+2+3'
print(eval(a))

def func(x):
    return x < 5
li = [1,2,55,56,5]
a = filter(func,li)
print(list(a))

def func1(x):
    return str(x) + 'hello'

a = tuple(map(func1,li))
print(a)

def func2(x):
    return x**3
a = tuple(map(func2,li))
print(a)

zip()  #配对
li1 = [1,2,3,4,5]
li2 = [7,8,9,10,11,12]

b = list(zip(li1, li2))
print(b)


name = 'wqe'
def me1():
    name = 'efds'
    print('1-----'+name)
me1()
print('2----'+name)

def me1():
    name2 = 'ad'
    def me2():
        print(name2)
    me2()
me1()

'''
函数内变量影响不到函数外变量
函数内可使用外部变量
'''
x = 123
def func():
    global x
    x = x + 100
    return x
a = func()
print(a)
print(x)
'''
函数内global修饰可以修改外部变量
'''
def func1():
    x = 123
    def func2():
        nonlocal x
        x = x + 500
        print(x)
    func2()
func1()
'''
内层函数使用nonlocal可以修改外层函数的变量
'''

'''
lambda 参数：表达式
'''

g = lambda a:a**2
print(g(5))

li = [1,2,3,4,5,6]
a = list(filter(lambda x:x>4, li))
for i in a:
    print(a)

a = filter(lambda x:True if x%2 == 0 else False, range(101))
print(list(a))

def func():
    def func1():
        return 'hello'
    return func1
print(func()())
'''
外层函数返回内层函数的引用
'''
li = []
for i in range(4):
    def func():
        return i
    li.append(func)

print(func())
for f in li:
    print(f())
'''
每次循环调用仅引用了函数，没有传值
'''

li = []
for i in range(4):
    def me1(i):
        def lili():
            return i
        return lili
    li.append(me1(i))

for f in li:
    print(f())
'''
调用me1函数的时候保存了参数i的值
'''

'''
计算阶乘
'''

def cal_factorial(n):
    if n > 1:
        return n * cal_factorial(n-1)
    else:
        return 1

print(cal_factorial(9))

