#__author:gzc
#date:2020/6/2
# -- coding: utf-8 --
#生成器使用的时候分配内存,不是一次性分配内存
#生成器是一个迭代对象

#生成器的两种创建方式
# (x for x in range(10))

# yield
a = (x*2 for x in range(10))

# for i in a:
#     print(i)

# foo() 是一个生成器对象
# def foo():
#     print("OK")
#     yield 1
#     print(1314)
#     yield 2
# g = foo()
# print(next(g))
# print(next(g))

# 斐波那契数列生成器
# def fib(max):
#     n,before,after=0,0,1
#     while max>n:
#         yield before
#         before,after= after,before+after
#         n= n + 1
#
# g = fib(10)
# for i in g:
#     print(i)

def bar():
    print("ok1")
    count =yield 1
    print(count)
    print("ok2")
    yield 2
b = bar()
# 第一次send前如果没有next() 需要传入None
b.send(None)
print(b.send("Hello"))
iter()