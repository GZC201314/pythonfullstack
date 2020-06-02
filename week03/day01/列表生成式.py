#__author:gzc
#date:2020/6/2
# -- coding: utf-8 --

#a=[x*x for x in range(10)]
def f(n):
    return n**3;
a=[f(x) for x in range(10)]
print(type(a))