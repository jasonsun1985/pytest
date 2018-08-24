#coding:utf8
#--coding:utf-8--
from http.server import HTTPServer,BaseHTTPRequestHandler     
import io,shutil,urllib     
#     
# class MyHttpHandler(BaseHTTPRequestHandler):     
#     def do_GET(self):     
#         if '?' in self.path:#如果带有参数
#             self.queryString=urllib.parse.unquote(self.path.split('?',1)[1])     
#             #name=str(bytes(params['name'][0],'GBK'),'utf-8')     
#             params=urllib.parse.parse_qs(self.queryString)     
#             print(params)     
#             name=params["name"][0] if "name" in params else None     
#         r_str="Hello "+name+" <form action='' method='POSt'>Name:<input name='name' /><br /><input type='submit' value='submit' /></form>"    
#         enc="UTF-8"    
#         encoded = ''.join(r_str).encode(enc)     
#         f = io.BytesIO()     
#         f.write(encoded)     
#         f.seek(0)     
#         self.send_response(200)     
#         self.send_header("Content-type", "text/html; charset=%s" % enc)     
#         self.send_header("Content-Length", str(len(encoded)))     
#         self.end_headers()     
#         shutil.copyfileobj(f,self.wfile)     
#     def do_POST(self):     
#         s=str(self.rfile.readline(),'UTF-8')#先解码     
#         print(urllib.parse.parse_qs(urllib.parse.unquote(s)))#解释参数     
#         self.send_response(301)#URL跳转     
#         self.send_header("Location", "/?"+s)     
#         self.end_headers()     
#     
# httpd=HTTPServer(('127.0.0.1',8888),MyHttpHandler)     
# print("Server started on 127.0.0.1,port 8888.....")     
# httpd.serve_forever()  
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
'''
mimedic = [
                        ('.html', 'text/html'),
                        ('.htm', 'text/html'),
                        ('.js', 'application/javascript'),
                        ('.css', 'text/css'),
                        ('.json', 'application/json'),
                        ('.png', 'image/png'),
                        ('.jpg', 'image/jpeg'),
                        ('.gif', 'image/gif'),
                        ('.txt', 'text/plain'),
                        ('.avi', 'video/x-msvideo'),
                    ]
'''
data = {'result': 'this is a test'}
host = ('localhost', 8888)
class Resquest(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'application/json')
#         self.end_headers()
#         self.wfile.write(json.dumps(data).encode())
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     }
        )
        self.send_response(200)
        self.end_headers()
#         self.wfile.write('Client: %sn ' % self.client_address[0] )
#         self.wfile.write('User-agent: %sn' % str(self.headers['user-agent']))
#         self.wfile.write('Path: %sn'%self.path)
        self.wfile.write(json.dumps(data).encode())
        for field in form.keys():
            field_item = form[field]
            print(field_item)
#             filename = field_item.filename
#             filevalue  = field_item.value
#             filesize = len(filevalue)#文件大小(字节)
            #print len(filevalue)
        #print (filename)
#             with open(filename.decode('utf-8'),'wb') as f:
#                 f.write(filevalue)
        return
if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()