# -*-coding:utf-8-*-
# 用于各种小测试
from TypesEnum import *


if __name__ == '__main__':

    import time
    t = time.localtime(time.time())
    import datetime
    a = datetime.date(*(t.tm_year, t.tm_mon, t.tm_mday))
    print(a, type(a))