#__author:gzc
#date:2019/4/20

import socket

sk = socket.socket()

address = ('127.0.0.1',8000)
sk.connect(address)

