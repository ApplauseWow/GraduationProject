# -*-coding:utf-8-*-
# rpc协议除基本数据类型以外的其他类型需要利用pickle模块序列化为字节流形式pickle.dump来传输


class ClientRequest(object):
    """
    客户端请求
    """

    def __init__(self):
        pass

    def get_note(self):
        pass