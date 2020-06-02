#__author:gzc
#date:2019/4/20

import socket
#  family type
#
sk = socket.socket()

address = ('127.0.0.1',8000)

sk.bind(address)
# 用于设置最多连接等待个数
sk.listen(5)

conn = sk.accept()

print(conn)
