# coding:utf-8
import time, datetime, functools,logging,os,shutil
from logging import _srcfile

logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename='common.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
#                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    '%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )


# 计算时间函数  
def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        logging.info('current Function [%s] run time is %.2f' % (func.__name__ , time.time() - local_time))  
    return wrapper


#移动文件
def move_file(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile, dstfile)
        print("move file %s -> %s "%(srcfile,dstfile))
        
#拷贝文件
def copy_file(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist ! " %(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copy(srcfile, dstfile)
        print("copy file %s -> %s " %(srcfile,dstfile))
            
