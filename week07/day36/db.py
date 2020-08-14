#__author:gzc
#date:2020/8/13
# -- coding: utf-8 --
import pymysql

conn = pymysql.connect(charset ='utf8',host='localhost',port=3306,user='root',passwd='abc123123',db='test')

# 创建游标
cursor = conn.cursor(cursor=dict)

# 执行sql 语句,并返回受影响的行数
# effect_row = cursor.execute('update teacher set tname = "孙运宏" where tid=3')
# print(effect_row)
# 执行多条sql语句,并返回受影响的行数
# student_list = [('钢蛋1', '女', 1),
#                 ('钢蛋2', '女', 2),
#                 ('钢蛋3', '男', 3),
#                 ('钢蛋4', '女', 3),
#                 ('钢蛋5', '女', 1),
#                 ('钢蛋6', '女', 2),
#                 ('钢蛋7', '男', 1),
#                 ('钢蛋8', '女', 3),
#
#                 ]
# effect_row = cursor.executemany('insert into student(sname,gender,class_id) values(%s,%s,%s)',student_list)
# # 执行修改数据库数据的操作时,需要执行提交操作
# conn.commit()
# cursor.execute('select * from student')
# # 返回一条记录
# student = cursor.fetchone()
# print(student)
# # 返回查询到的所有记录
# # studentlist = cursor.fetchall()
# # 指定返回的记录条数
# studentlist = cursor.fetchmany(3)
# for student in studentlist:
#     print(student)

# 执行存储过程
result = 0
r1 = cursor.callproc('p1',args=(1,'郭德纲','男',result))
# 返回结果集
result1=cursor.fetchall()
print(result1)
cursor.execute('select @_p1_0,@_p1_1,@_p1_2,@_p1_3')
# 返回out变量
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()