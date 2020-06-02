#__author:gzc
#date:2018/11/6
from functools import reduce
def func(n):
    if(n%2==0):
        return n

def func1(n):
    return '$==='+n+'===$'
def func2(x,y):
    return x+y
arr = ['1','2','3']
arr1 = [1,2,3,4,5,6,7,8,9,10]

# 对列表进行过滤
# ret = filter(func,arr)
# print(list(ret))

# 对列表进行处理
# ret = map(func1,arr)
# print(list(ret))

ret = reduce(func2,arr1)
print(ret)