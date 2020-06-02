# __author:gzc
# date:2019/1/2

def foo():
    print('Hello')

import pickle

f = open('pickle_text','rb')

fun = f.read()
fun = pickle.loads(fun)
fun()

f.close()