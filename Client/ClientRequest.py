# -*-coding:utf-8-*-
# rpc协议除基本数据类型以外的其他类型需要利用pickle模块序列化为字节流形式pickle.dump来传输
from rpc_protocol import correspondence_pb2, correspondence_pb2_grpc
import grpc
from TypesEnum import *
try:
    import cPickle as pickle
except:
    import pickle


class CR(object):
    """
    客户端请求连接
    """

    _host = '192.168.2.104:44967'

    def __init__(self):
        self.channel = grpc.insecure_channel(self._host)
        self.stub = correspondence_pb2_grpc.BackendStub(self.channel)

    def CloseChannnel(self):
        self.channel.close()

    def SayHelloRequest(self):
        """
        用于测试
        :return:
        """

        response = self.stub.SayHello(correspondence_pb2.HelloRequest(para=pickle.dumps('test')))
        print(pickle.loads(response.result), type(response.result))

    def GetNotesCountRequest(self, table):
        """
        获取总记录条数
        :param table: 表名　不应该暴露表名　修改！！！
        :return: 条数
        """

        try:
            data = {'table': table}
            response = self.stub.GetRecordsCount(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:  # 请求失败
                return 0
            elif res['operation'] == ClientRequest.Success:  # 请求成功
                return res['result']
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def GetAllNotesRequest(self, start=None, num=None):
        """
        获取所有公告
        :param start:　起始位置
        :param num:　每页条数
        :return:{'valid':, 'invalid:'}
        """

        try:
            data = {'start': start, 'num': num}
            response = self.stub.GetAllNotes(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:  # 请求失败
                return {'valid': (), 'invalid': ()}
            elif res['operation'] == ClientRequest.Success:  # 请求成功
                return res['result']
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')


if __name__ == '__main__':
    conn = CR()
    print conn.GetAllNotesRequest()



