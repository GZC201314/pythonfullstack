# __author:gzc
# date:2018/11/24
'''
用户输入一个运算式,通过正则解析来获取最后的计算结果
'''
#
import re
def check(s):
    flag=True
    if re.findall('a-zA-Z',s):
        print('Invalid')
        flag = False
    return flag
def format(s):
    s = s.replace(' ','')
    s = s.replace('++','+')
    s = s.replace('+-','-')
    s = s.replace('--', '+')
    return s

def cal_mul_div(s):

    return s

def cal_add_sub(s):

    return s



# 1. 获取用户输入的运算式
s = input('请输入一个运算式 :  ')
if check(s):
    s = format(s)

    # 如果匹配到了最里边的括号
    # 判断是否有括号
    while re.search('\(',s):
        substr = re.search(r'\([^()]+\)', s).group()
        substr = cal_mul_div(substr)
        substr = cal_add_sub(substr)
    else:
        s = cal_mul_div(s)
        s = cal_add_sub(s)
