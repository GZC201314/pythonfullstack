#__author:gzc
#date:2020/7/28
# -- coding: utf-8 --

import queue

d = queue.Queue(5)
count=0
while d.full() is not True:
    d.put(count)
    count+=1
while d.empty() is not True:
    print(d.get())
