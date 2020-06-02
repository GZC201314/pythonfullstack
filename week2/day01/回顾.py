#__author:gzc
#date:2018/11/5

# s2 = set(['gzc'])
# s2.update('123')
# print(s2)

# 高阶函数

def f(n):
    return n*n

def foo(a,b,f1):
    return f1(a)+f1(b)

print(foo(1,2,f))
