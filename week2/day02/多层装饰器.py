# author:gzc
# date:2018/11/10
import time
def action(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('log.txt','a') as f:
        f.write('%s end action %s\n'%(time_current,n))
def logeer(flag):
    def show_time(f):
        start = time.time()
        def inner(*x,**y):
            f(*x,**y)
        end = time.time()
        print("程序运行时间是  :",(end-start))
        if(flag=="true"):
            action(end-start)
        return inner
    return show_time

@logeer("false")
def add(*a,**b):
    sum=0
    for i in a:
        sum +=i
    print("和是   :", sum)


add(1,2,3,4,5,6,6,7,8,8,9,9,9,99,9,90)