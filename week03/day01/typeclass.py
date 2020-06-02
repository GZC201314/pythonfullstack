#__author:gzc
#date:2019/3/21

class Mytype(type):
    def __init__(self,*args,**kvargs):
        print(123)
        pass

class Foo(object,metaclass=Mytype):
    stat = "123"
    def func(self):
        print("Hello Mytype")


# obj = Foo()
import s1
import url1
# var = getattr(Foo,'stat')
# print(s1.NAME)
# # print(s1.func())
url = input("请输入URL： ")
if hasattr(url1,url):
    func = getattr(url1,url)
    var = func()
    print(var)
else:
    print('404')
