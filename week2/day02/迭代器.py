#__author:gzc
#date:2020/6/2
# -- coding: utf-8 --
from collections.abc import Iterator,Iterable
l = [1,2,3,5]
d = iter(l);
print(d)

print(isinstance(l,list))
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
print(isinstance(d,Iterator))