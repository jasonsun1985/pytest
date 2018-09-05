#!/usr/bin/python3
#coding:utf-8
import com.test.basepy, com.test.util, logging
from com.test.util import move_file, copy_file
from _functools import reduce
from io import StringIO
import os
import pickle
import json

# from builtins import int
# from idlelib.iomenu import encoding
spider = """                              `
         `                    `
         ,                    '
         :                     &   
         '                     `
         +                     ,
         #                     '
         @                     #
         @                     @
         @                     @
         @                     @
         @                     @
         @                     @
         #,                   `@
         ,#                   ;'
          @                   #,
          @                   @
          #,                  @          `
          ,#                  @         ,
           @                 ,@
 :         @                 +'        +
  #        @.                @.       #
   ;       :#                @       ;,
   :.       @               `@      `@
    @       @.              @;      @
     @`     .@             ;@      @,
     `@.     #@            @.     @'
      `@:     @:          #@     @@
       `@;    .@         `@     #@
         @#    #@        @+    @@
          @@`   @'      ,@   `@+
           ,@+  .@` . ` @;  ,@,
             #@  #@;'@+@@  +@
              ,@; @;@@@@, @#
                #@#+@@@@;@;
                 .@+@@@@@`                ,
                   :@@@@@               `,
  ;              `#@'@@@@@@:           #`
   ;:          ;@@+@'@@@@ ,#@@+.``   :@
    `@,   `,'@@+` `;@@@@@#    ,'##@@@@
      #@@@#',     ;@@@@@@@
                 .;@@@@@@@#
                 @;@@''+@@@#
                #@;@@+'@@@@@
                @';@@''@@@@@@
               '@`;#@''#@@' @`
               @. ';@@@@@@  #@
              .@  `;;@@@@   `@
              #@   ,;;+@     @;
              @:             ;@
              @`             .@
              @               @
              @               @`
             `@               @;
             ,@               ##
             ;@               :@
             +#               `@
             @+                @
             @,                @.
             @`                +:
             #`                @
              #                '
              '               ;
               ;              +
               :
                .            :
                `"""
print(spider)
list1 = ["a", 123, 4.3]
tinylist = [123]
if 123 in tinylist:
    print(123, "in tinylist")
else:
    print(123, "not in")
tuple1 = (1, 2, 3, 4, 4, 5)
tuple2 = (3, 2, 3, 4, 5)
print(tuple1[2:-2])
for x in (list1):
    print(x * 2)
    '''print(list)'''
flag = True
print(flag)
a = "A"
b = "B"
if a == b:
    print("a = b ") 
    
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
# birth = int(input("birth:"))  int函数下面birth为数值型即可
'''
birth = input("birth:")
if (birth >='1980' and birth <'1990'):
    print("80 后")
elif (birth >='1990' and birth <'2000'):
    print("90 后")
elif (birth >='2000' and birth <'2010'):
    print("00 后")
elif (birth >='2010' and birth <'2020'):
    print("10 后")

身高1.77，体重88kg。请根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数：
    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖

height = float(input("请输入你的身高："))
weight = float(input("请输入你的体重："))
result = weight/height**2
print(result)
if(result <18.5):
    print("过轻")
elif(result>18.5 and result <25):
    print("正常")
elif(result>25 and result <28):
    print("肥胖")
elif(result>28 and result <32):
    print("严重肥胖")
'''
sum = 0
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum += num
print("sum is ", sum)
    
sum = 0
for n in range(100):
    sum += n
print(sum)

sum = 0
n = 90
while n > 0:
    sum += n
    n -= 2
print(sum)

m = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(m['Michael'])
print(m.get('Michael'))
print(m.pop('Michael'))
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.remove(3)
print(s)
s2 = set([1,3,4])
s3 = set([1,2,4])
print(s2&s3)
print(s2^s3)
print(s2|s3)

n1 = 255
print("255 16进制 ",hex(n1))
print("0xff 10进制 ",int(0xff))


def my_method(x,y):
    return x*y
x=1
y=2
print(my_method(x, y))

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print(my_abs(10))

str3="GOOD"
for s in str3:
    print(s,end=" ")
    print(s.join("-*-"))
    #help(print)
liuliang = "{u:.1f}{uu}".format(u=28.8888,uu="GB")
print(liuliang)
str4 = "I YOU"
print(str4[:1]+" LOVE"+str4[1:])
f1="I am {0}, i am {1}d years old".format("jason", 33)
print(f1)
f2 = "i am {name}, i am {age}d years old".format(**{"age":33,"name":"jason"})
print(f2)
f3 = "--{name:*^10s}--   =={age:<10.2f}==".format(name='jason',age=33.8888)   #将name的宽度设置为10,空余的使用*号不全,并居中显示,age类型设置为浮点型,宽度为10.并左对齐
print(f3)
f4 = "原数d:{:d}  二进制b:{:b}, 八进制o:{:o}, 十六进制x:{:x}".format(33, 33, 33, 33)   #进制转换
print(f4)
f5 = "原数:{:d}, 科学计数法e:{:e}, 科学计数法E:{:E}" .format(1000000000,1000000000,1000000000)    #科学计数法表示
print(f5)
f6 = "原数:{:2F}, 百分号表示{:.2%},  原数:{:d},自动分割表示:{:,}".format(0.75,0.7584,10000000,10000000 )  #百分号表示及自动分割
print(f6)
'''递归
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
def fact(m):
    if m==1:
        return 1
#     print(m,"*fact(",m,"-1)")
    return m*fact(m-1)
print(fact(5))

str5 = "<img id=\"blogLogo\" src=\"/Skins/custom/images/logo.gif\" alt=\"返回主页\">"
print(str5)

fpath=r'D:\temp\new 4.txt'
# with open(fpath,'r',encoding='utf-8') as f:
#     s = f.read()
#     print(s)
f=open(fpath,'r',encoding='utf-8')
for line in f.readlines():
    print(line)
ll={"as",20}
print(ll)
li=[]
for i in range(10):
    li.append(str(i))
print("|".join(li))

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
result1 = dict(zip(names,scores))
print(result1)
print("[1,2,3,4] 是 tuple 吗 ？ ",isinstance([1,2,3,4],tuple))
print("{1:2,3:4} 是 dict 吗 ？ ",isinstance({1:2,3:4},dict))
#进制转换
print(int('10', base=8))
print(int('10', base=2))
print(int('10', base=16))

# move_file(r"D:\self\图片\time.jpg", r"D:\self\图片\timeeeeeee.jpg")
# copy_file(r"D:\self\图片\time.jpg", r"D:\self\图片\timeeeeeee.jpg")
fw=open('D:/test.txt', 'wb')#a文件追加
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
pickle.dump(d, fw)
fw.close()
frr=open('D:/test.txt', 'rb')#一定加b
fileInfo=pickle.load(frr)
print(fileInfo)

def f(x):
    return x**x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
def add(x,y):
    return x+y
rr=reduce(add,[1,2,3])
print(rr)
def fn(x,y):
    return x*2+y
rrr=reduce(fn, [1,2,3,4]) #reduce(lambda x,y:x*2+y, [1,2,3,4])
print(rrr)
#保留奇数
def is_odd(n):
    return n % 2 == 1
r1=filter(is_odd,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list(r1) :",list(r1))

def _odd_iter():
    n=1
    while True:
        n+=2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it=filter(_not_divisible(n),it)
# print("素数： ",primes())
rn=list()
for n in primes():
    if n <100:
        print(n)
        rn.append(n)
    else:
        break
print("素数的个数为：%s " % len(rn))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
for x in os.listdir('.'):
   print(x)
# '/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
print(json.dumps(d))
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student("jason", 18,100)
print(json.dumps(s,default=student2dict))

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print("a和b的差集 ",a - b)     # a和b的差集
print("b和a的差集 ",b - a)     # b和a的差集
print("a和b的并集 ",a | b)     # a和b的并集
print("a和b的交集 ",a & b)     # a和b的交集
print("a和b中不同时存在的元素 ",a ^ b)     # a和b中不同时存在的元素