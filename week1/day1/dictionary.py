#__author:gzc
#date:2018/8/26

# 字典的遍历
dic = dict(name='郭志超', age=26, hobby='足球')

# 最直接,效率高
# for i in dic:
#     print(i,dic[i])

# 效率低 不建议使用
# for i,v in dic.items():
#     print(i,v)

# dic1 = {'name':'张三','python':'1234'}
# print(dic['hobby'])

# setdefault 有则取相关的值,没有则添加
# ret = dic.setdefault('name1','gzc')
# print(dic)
# print(ret)

# print(list(dic.keys()))
# print(list(dic.values()))
# print(list(dic.items()))
# dic.update(dic1)
# print(dic)
# print(dic1)
#
# del dic['name']
# dic.clear()


# dic3 = dic.fromkeys(['key4','key2','key3'],'test')
#
# print(sorted(dic3.items()))