# -*-coding:utf-8-*-
import grpc
import correspondence_pb2, correspondence_pb2_grpc  # *_pb2是用于数据类型定义, *_pb2_grpc是用于通信接口定义
from concurrent import futures
import time
from CallMethodImplement import *
try:
    import cPickle as pickle
except:
    import pickle

_MAX_WORKER = 10
_PERMIT_CLIENTS_AND_PORT = '[::]:50050'
_ONE_DAY_IN_SECONDS = 60*60*24


class BackendService(correspondence_pb2_grpc.BackendServicer):

    # 实现proto文件里定义的rpc调用接口
    def SayHello(self, request, context):
        ip = str(context.peer()).split(':')[1]  # 客户端ip
        data = pickle.loads(request.para)  # 请求参数
        # 业务实现函数
        # func(ip = ip, data = data)
        SayHelloImplement(ip = ip, data = data)
        return correspondence_pb2.HelloResponse(result = bytes('test'))

    def SayHelloAgain(self, request, context):
        ip = str(context.peer()).split(':')[1]  # 客户端ip
        data = pickle.loads(request.para)  # 请求参数
        # 业务实现函数
        # func(ip = ip, data = data)
        return correspondence_pb2.HelloResponse(result = bytes('test'))


def service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=_MAX_WORKER))
    correspondence_pb2_grpc.add_BackendServicer_to_server(BackendService(), server)
    server.add_insecure_port(_PERMIT_CLIENTS_AND_PORT)
    server.start()
    # 一直阻塞保持服务状态，当ctrl+C时停止服务
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt as e:
        print("stop the service")
        server.stop(0)

if __name__ == '__main__':
    service()
