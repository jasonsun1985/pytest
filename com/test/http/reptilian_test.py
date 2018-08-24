#coding:utf-8
'''
Created on 20180824
@author: R07400
'''

from bs4 import BeautifulSoup
import requests

#get(从服务器获取数据)/post（向服务器提交数据）

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'Referer':'https://www.baidu.com/link?url=v5mEpioigrLXdyiGfy8kMlTTxP62rNNw2ZC03jZw0Yu7Z5Aj5fRrAkRmiccLwY4X&wd=&eqid=f6ad6aef00000c6e000000065b7fd453',
    'Host':'www.weather.com.cn'
    }

req=requests.get('http://www.weather.com.cn/',headers=headers)

print(req.content.decode("utf-8"))