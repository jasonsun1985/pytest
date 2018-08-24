#coding:utf-8
import time,datetime,functools,logging
from com.test.util import print_run_time


# #计算时间函数  
# def print_run_time(func):  
#     def wrapper(*args, **kw):  
#         local_time = time.time()  
#         func(*args, **kw) 
#         logging.info('current Function [%s] run time is %.2f' % (func.__name__ ,time.time() - local_time))  
#     return wrapper
@print_run_time
def fast(x, y):
    time.sleep(1.2)
    return x + y;

f = fast(11, 22)
