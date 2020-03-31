# -*-coding:utf-8-*-
import time
from TypesEnum import *


LOG_PATH = "./client_log"

def log(client_ip, client_req):
    """
    装饰器－记录客户端请求日志
    :param client_ip:客户端ip
    :param client_req:客户端请求
    :return: None
    """

    def wrapper(func):
        def deco(*args, **kwargs):
            res = func(*args, **kwargs)
            if res['operation'] == DBOperation.Failure or ProcessOperation.Failure:  # 操作失败
                record = "{} : {} at {}, but fail, as {}\n".format(client_ip, client_req, time.asctime(time.localtime(time.time())), res['exception'])
                with open(LOG_PATH, 'a') as f:
                    f.write(record)
                return res
            elif res['operation'] == DBOperation.Success or ProcessOperation.Success:  # 操作成功
                return res
        return deco
    return wrapper