#coding:utf-8
from enum import unique, Enum


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
        
day1 = Weekday.Mon
print(day1)
print("英文  {0} 阿拉伯数字 {1} ".format(day1.name,day1.value))
print("英文  %s 阿拉伯数字 %s " %(day1.name,day1.value))