#coding:utf-8
'''
Created on 20180824
@author: R07400
'''
import requests
#GET
# r = requests.get("http://127.0.0.1:8888?name=aaa")
# print(r.text)
#POST
postdata = {'name':'JASON',"age":33}
r = requests.post("http://127.0.0.1:8888",data=postdata)
print(r.text)