# -*-coding:utf-8-*-
# rpc协议除基本数据类型以外的其他类型需要利用pickle模块序列化为字节流形式pickle.dump来传输
import correspondence_pb2, correspondence_pb2_grpc
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
        self.channel = grpc.insecure_channel('192.168.2.104:449')
        self.stub = correspondence_pb2_grpc.BackendStub(self.channel)

    def SayHelloRequest(self):
        response = self.stub.SayHello(correspondence_pb2.HelloRequest(para = bytes('test')))
        print(response)

if __name__ == '__main__':
    channel = grpc.insecure_channel('192.168.2.104:50050')
    # 调用 rpc 服务
    stub = correspondence_pb2_grpc.BackendStub(channel)
    print stub.SayHello(correspondence_pb2.HelloRequest(para = bytes('test')))