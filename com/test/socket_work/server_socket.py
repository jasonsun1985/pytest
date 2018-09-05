#coding:utf-8
import threading
import time
import socket

def tcplink(sock,addr):
    print("接受来自  %s 的连接 ,当前的线程为： %s " % (str(addr),threading.current_thread().name))
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        received = data.decode('utf-8')
        print("服务端收到客户端信息 %s " %received)
        sock.send(("success received !").encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.bind(("127.0.0.1",8080))
    s.listen(5)
    print("等待连接...")
    while True:
        sock,addr=s.accept()
        t=threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
except Exception as e:
    print(e)
finally:
    pass