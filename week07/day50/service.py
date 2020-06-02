#__author:gzc
#date:2019/4/20

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data,"utf8"))
                print("waiting....")
                conn.sendall(client_data)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),MyServer)
    server.serve_forever()