#__author:gzc
#date:2018/8/21
_USER_='GZC'
_PASSWORD_='abc123'

for i in range(3):
    name = input('Name: ')
    password=input('Password: ')
    if(name==_USER_ and password==_PASSWORD_):
        print("Welcome %s login" % (name))
        break
    else:
        print('Invalid username or password.')
else:
    print('错误的次数达到上限,程序已退出.')