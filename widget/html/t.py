import time

def timer(func):
    def wrapper(*args, **kwargs):  #装饰函数
        print("This is wrapper function.")
        startTime = time.time()
        res = func(*args, **kwargs)   #调用基础函数；外层为添加的功能
        endTime = time.time()
        usedTime = (endTime - startTime)*1000  #乘1k单位为ms
        print("Use time: %d ms"%usedTime)
        return res
    return wrapper

charList = [chr(i) for i in range(97,123)]
CharList = [chr(i) for i in range(65,91)]
li3 = [i for i in range(10)]


print(li3)
#usrIdList = [i for i in range()]

