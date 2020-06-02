#__author:gzc
#date:2018/9/1

# r+ 读写模式 w+ 写读模式 a+ 追加模式
file = open('city','r',encoding='utf-8')
# # # print(file.read())
# # # print('555',file.read(5))
# # file1 = open('city1','w',encoding='utf-8')
# # file1.write(file.read())
# # print(file.fileno())
# count=0
# for i in file.readlines():
#     count+=1
#     if count ==6:
#         i = ''.join([i.strip(),'gzc'])
#     print(i.strip())

# for i,v in enumerate(file.readlines()):
#     if i ==6:
#         v= ''.join([v.strip(),'gzc'])
#     print(v.strip())

# print(file.read(4))
# seek()重置光标的位置
# file.seek(9)
# print(file.read(4))


# # 下载进度条
# import sys,time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(1)


# 判断是不是一个终端
# print(file.isatty())
# print(file.readable())
#把字符串转换成字典类型
# eval()

# file.truncate(5)


# file.flush()
# file.close()
# # file1.close()





