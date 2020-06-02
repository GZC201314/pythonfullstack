#__author:gzc
#date:2018/10/30
import time

def action(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('log.txt','a') as f:
        f.write('%s end action%s\n'%(time_current,n))

action(10)
