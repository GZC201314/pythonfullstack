#__author:gzc
#date:2019/3/26
class singleclass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

# v =None
#
# while True:
#     if v:
#         v.show()
#     else:
#         v= singleclass('gzc','24')
#         v.show()

class Foo:
    __v =None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v


obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)