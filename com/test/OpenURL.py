#-*- coding:utf-8 -*-
'''
Created on 2018年8月15日
打开URL
@author: R07400
'''
from html.parser import HTMLParser
import urllib.request
import com.util.MyHTMLParser
from com.util.MyHTMLParser import parser

str1=input("请输入JIRA单号:")
url="http://172.17.189.93:8080/browse/RIILBUG-"+str1
print('你输入的单号为：',str1,'\n即将打开URL: ',url)
headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                'Upgrade-Insecure-Requests': '1',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                # 'Accept-Encoding': 'gzip, deflate',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
req = urllib.request.Request(url=url, headers=headers)
try:
    resp = urllib.request.urlopen(url)
    html = resp.read()
    html = html.decode("utf-8")
    print(html)
    parser.handle_starttag('meta', 'name')
except:
    print('页面不存在： ' + url)
