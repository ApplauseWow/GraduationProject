# -*-coding:utf-8-*-
# rpc协议除基本数据类型以外的其他类型需要利用pickle模块序列化为字节流形式pickle.dump来传输
from rpc_protocol import correspondence_pb2, correspondence_pb2_grpc
import grpc
try:
    import cPickle as pickle
except:
    import pickle

class CR(object):
    """
    客户端请求连接
    """

    def __init__(self):
        self.channel = grpc.insecure_channel('192.168.2.104:44967')
        self.stub = correspondence_pb2_grpc.BackendStub(self.channel)

    def SayHelloRequest(self):
        """
        用于测试
        :return:
        """
        response = self.stub.SayHello(correspondence_pb2.HelloRequest(para = pickle.dumps('test')))
        print(pickle.loads(response.result), type(response.result))

