# __author:gzc
# date:2018/11/22
import hashlib

md5 = hashlib.md5()
md5.update('hello world'.encode('utf8'))
print(md5.hexdigest())