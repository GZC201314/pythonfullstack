# author:gzc
# date:2018/11/8
import time
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end-start)
    return inner
# @show_time
# def foo():
#     print('foo....')
#     time.sleep(2)
# @show_time
# def bar():
#     print('bar....')
#     time.sleep(3)

