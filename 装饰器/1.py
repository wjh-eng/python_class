
import time
string = 'dsfsdfgergrdgfdhgfhkhjkhjk'
def modifty(func):
    def wrapper(string):
        a = time.time()
        for i in range(10000000):
            func(string)
        b = time.time()
        return b-a
    return wrapper

@modifty
def test_type(string):
    type(string)
@modifty
def test_isinstance(string):
    isinstance(string,str)

print(test_type(string))
print(test_isinstance(string))
