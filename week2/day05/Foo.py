#__author:gzc
#date:2019/1/30
class Foo:

    @property
    def sta(self):
        print("staticmethod")

    @classmethod
    def clas(cls):
        print('classmethod')
if __name__== '__main__':
    Foo.clas()
    obj = Foo()
    obj.sta