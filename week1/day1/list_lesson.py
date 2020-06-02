# __author:gzc
# date:2018/8/22
# 列表的基础知识
a = ['abc', 'efg', 'gzc', 'xyz', 'asd']

# 查 切片
# print(a[1])
# print(a[0:])
# print(a[0:-1])
# print(a[0::2])
# print(a[3::-2])

# 新增
# a.append('Hello')  # 默认插到最后一个位置
# a.insert(1, 'GZC')  # 将数据插入到指定的位置
# print(a)

# 删除
# a.remove('GZC')#通过内容来删除元素
# print(a)
b = a.pop(0)#通过索引来删除元素,并返回删除的元素内容
# del a[0]
# print(a)
# print(b)

# 查询某个元素在列表中出现的次数
# a=['to','be','or','not','to','be']
# # print(a.count('to'))


# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# print(b)

# index
# a = ['to', 'be', 'or', 'not', 'to', 'be']
# print(a.index('not'))
# print(a.index('to'))

# a = ['to', 'be', 'or', 'not', 'to', 'be']
#
# first_to_index = a.index('to')
# first_to_list = a[first_to_index + 1:]
# second_to_index = first_to_list.index('to')
# print(a[first_to_index + second_to_index + 1])

# reverse
# a = ['to', 'be', 'or', 'not', 'to', 'be']
# a.reverse()
# print(a)

# a = [4, 6, 2, 1, 7, 9]
# a.sort(reverse=True)
# print(a)
