#__author:gzc
#date:2019/6/23
# -- coding: utf-8 --
import subprocess

obj = subprocess.Popen("dir",shell="True",stdout=subprocess.PIPE)
print(str(obj.stdout.read(),'gbk '))