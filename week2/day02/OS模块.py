# __author:gzc
# date:2018/11/21

import os

# E:\\mysql
# 重命名文件
# os.rename('log.txt','log1.txt')

# 获取文件信息 st_size 文件大小  st_atime 上一次被访问的时间 st_mtime 上一次修改的时间
# filemsg = os.stat('log1.txt')
# print(filemsg)

# 获取当前系统的路径分隔符
# print(os.sep)

# 获取换行分隔符
# print(os.linesep)

# 用于执行shell命令
# dir = os.system('dir')
# print(dir)

# 获取文件的绝对路径
# print(os.path.abspath('log1.txt'))

# 获取文件夹路径,和文件名
# s = os.path.split('E:\\fullstack\\week2\\day02\\log1.txt')
# print(s)

# 获取文件的文件夹路径
# print(os.path.dirname('E:\\fullstack\\week2\\day02\\log1.txt'))
# print(os.path.join('E:\\fullstack\\week2\\day02\\','log1.txt','log123.txt'))

# 删除文件
# os.remove("G:/新建文件夹/")
# 删除空文件夹
# os.removedirs("G:/新建文件夹/")

# 文件夹下面的文件信息

list = os.listdir("G:/新建文件夹/")

for i in list:
    print(i)

