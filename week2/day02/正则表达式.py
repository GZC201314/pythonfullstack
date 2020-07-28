#__author:gzc
#date:2020/6/21
# -- coding: utf-8 --
# 正则表达式

import re

s = 'hello world'

# print(re.findall('hello','hello world'))

# . 元字符 用于匹配一个字符(不包括换行符\n)
# ret = re.findall('w..l','hello world')

# ^ 用于开始匹配
# ret = re.findall('^h...o','hello hello')

# $ 用于末尾匹配

# ret = re.findall('hello$','hello hell0')

# * 用于重复匹配[0,+00]
# ret = re.findall('h*','hhllo')

# + 用于重复匹配[1,+00]
# ret = re.findall('h+l','hl')

# ? 用于重复匹配[0,1]
# ret = re.findall('h+l','hhl')

# {} 用于重复匹配
# ret = re.findall('a{1,3}b','aab')

# [] 用于字符集匹配,取消元字符的特殊功能
# ret = re.findall('a[bcbd]b','abb')
# ret = re.findall('[1-9a-zA-Z]','12tyAS')

# ^放在[]里,用于取反
# ret = re.findall('[^4,5]','45a')

#  \ 后面用于去除特殊功能,后面跟普通字符实现特殊功能
# \d 匹配任何十进制数
# \D 匹配任何非数字字符
# \s 匹配任何空白字符
# \S 匹配任何非空白字符
# \w 匹配任何字母数字字符
# \W 匹配任何非字母数字字符
# \b 匹配一个特殊字符边界,也就是指单词和空格间的位置
# ret = re.findall('\d{11}','15611122231q')
# ret = re.findall('\Wasd','a asd')
# ret = re.findall(r'I\b','I am a LIST')

############################################################
# 获取匹配到的内容

# 正则分组
# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt234/ooo')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))
# print(re.search('123','abc123').group())

# 正则表达式的方法

# findall() 所有的结果都返回到一个列表里边
# search()  返回匹配到的第一个对象,对象可以调用group()方法返回结果
# match()   只在字符串开始匹配,也返回匹配到的第一个对象,对象可以调用group()方法返回结果
# split()   可以用元字符进行匹配
# sub()     可以用于匹配替换
# compile() 批量正则匹配处理

# ret = re.split('\d{1}','abc1qwqe2sda')
# ret = re.split('[j,s]','dsajkdnas')
# ret = re.sub('a..x','s..b','hfabcxxx')
obj = re.compile('\.com')
ret  = obj.split('www.abc.com')
print(ret)






