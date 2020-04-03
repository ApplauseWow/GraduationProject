# -*-coding:utf-8
# 封装rpc请求函数
from Log import log
from TypesEnum import *


@log
def SayHello(ip, data):
    """
    用于测试
    :param ip:
    :param data:
    :return:
    """
    d = dict()
    d['operation'] = DBOperation.Failure
    d['exception'] = Exception('fail to ...')
    return d