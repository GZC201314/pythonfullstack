#__author:gzc
#date:2018/8/26

# a='123'
# # b='abc'
# # c=a+b
# # print(c)
# # c=''.join([a,b])
# # print(c)


st='hello kitty {name} is {age}'
print(st.count('1'))
print(st.capitalize())
print(st.center(50,'#'))
print(st.endswith('tty3'))
print(st.startswith('he'))
print(st.find('y'))
print(st.format(name='gzc',age=37))
print(st.format_map(({'name':'alex','age':37})))
print(st.index('t'))
print('abc123'.isalnum())#字符串只包含字母或者数字 返回True or False

print('123'.isdigit()) #必须是一个整数

print('1234'.isdecimal()) #判断是否是一个十进制的数

print('GZC is a boy'.lower())
print('GZC is a boy'.upper())
print('GZC is a boy'.swapcase())
print('GZC is a boy'.ljust(50,'*'))
print('GZC is a boy'.rjust(50,'*'))
print('   GZC is a boy'.strip())
print('GZC is a boy'.replace('GZC','zhangsan'))
print('GZC b is a boy'.rfind('b'))#从右向左找,找出第一个索引位置
print('GZC is a boy'.rsplit(' '))
print('&&'.join('GZC is a boy'.rsplit(' ')))