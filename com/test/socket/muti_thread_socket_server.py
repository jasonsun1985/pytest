#coding:utf-8
import threading
import socketserver
import time

class tcp_server_handler(socketserver.BaseRequestHandler):
    def handle(self):  #所有请求的交互都是在handle里执行的,
        while True:#循环收发数据包，长连接
            try:
                self.data = self.request.recv(1024).strip()#每一个请求都会实例化tcp_server_handler(socketserver.BaseRequestHandler):
                time.sleep(2)
                print("当前的线程为： %s " %threading.current_thread().name)
#                 print("{0} wrote:".format(self.client_address[0]))
#                 print(self.data.decode("utf-8"))
                self.request.sendall(self.data.upper())#sendall是重复调用send.
#                 if xxx 通过if条件可以终止长连接
            except ConnectionResetError as e:
                print("err ",e)
                break

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8080 #本地windows
#     HOST, PORT = "0.0.0.0", 9999  #本地Linux
    s = socketserver.ThreadingTCPServer((HOST, PORT), tcp_server_handler)   #线程
#     server = socketserver.TCPServer((HOST, PORT), tcp_server_handler)   #线程
    s.serve_forever()