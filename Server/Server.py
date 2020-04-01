# -*-coding:utf-8-*-
import grpc
import server_pb2, server_pb2_grpc  # *_pb2是用于数据类型定义, *_pb2_grpc是用于通信接口定义
from concurrent import futures
import time
try:
    import cPickle as pickle
except:
    import pickle


_MAX_WORKER = 10
_LIMIT_CLIENTS_AND_PORT = '[::]:44967'
_ONE_DAY_IN_SECONDS = 60*60*24


class BackendService(server_pb2_grpc.BackendServicer):

    # 实现proto文件里定义的rpc调用函数
    def SayHello(self, request, context):
        return server_pb2.HelloResponse(result = pickle.dumps("456"))

    def SayHelloAgain(self, request, context):
        return server_pb2.HelloResponse(result = pickle.dumps("123"))


def service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=_MAX_WORKER))
    server_pb2_grpc.add_BackendServicer_to_server(BackendService(), server)
    server.add_insecure_port(_LIMIT_CLIENTS_AND_PORT)
    server.start()
    # 一直阻塞保持服务状态，当ctrl+C时停止服务
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt as e:
        print("stop the service")
        server.stop(0)



