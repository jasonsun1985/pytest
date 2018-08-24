#-*- coding:utf-8 -*-
'''
Created on 2018年8月16日
@author: R07400
'''
def hannuota(n,x,y,z):
    if n==1:
        print(x+"->"+z)
    else:
        hannuota(n-1, x, z, y)
        print(x+"->"+z)
        hannuota(n-1, y, x, z)
def start():
    try:
        n=int(input("请输入汉诺塔层数："))
        while n < 3:
            print("汉诺塔从三层开始,请重新输入")
            n = int(input("请输入汉诺塔层数："))
            if n >=3:
                break
        hannuota(n, "A", "B", "C")
    except ValueError as e:
        print(e)
        start()
if __name__ == '__main__':
    start()