#coding: utf-8
import socket

try:
    hostport = ("127.0.0.1",8080)
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建TCP socket
    c.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
    c.connect(hostport)  #链接套接字
    
    while True:
        user_input = input('>>>:').strip()
#         s.send(bytes(user_input,'utf8')) #发送数据到套接字
        c.send(user_input.encode(encoding='utf_8')) #发送数据到套接字
        if not len(user_input):continue
        if user_input == 'quit':
            c.close()
            break
        server_reply = c.recv(1024) #接收套接字数据

        print(str(server_reply, 'utf8')) #打印输出
except Exception as e:
    pass
finally:
    pass