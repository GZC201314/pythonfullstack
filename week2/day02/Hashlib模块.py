# __author:gzc
# date:2018/11/22
import hashlib

# md5 = hashlib.md5()
# md5.update('hello world'.encode('utf8'))
# print(md5.hexdigest())
#
# m2 = hashlib.md5()
# m2.update('hello worldgzc'.encode('utf8'))
# print(m2.hexdigest())


sha = hashlib.sha256()
sha.update('hello world'.encode('utf8'))
print(sha.hexdigest())
