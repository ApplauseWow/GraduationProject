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

    _HOST = 'localhost'  # 192.168.
    _PORT = '44967'

    def __init__(self):
        self.channel = grpc.insecure_channel("{server}:{port}".format(server=self._HOST, port=self._PORT))
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

    # 共用
    def GetCountRequest(self,obj,  _type=None):
        """
        获取总记录条数
        :param obj: 对象 eg: 'note', 'project' 'user' ...
        :param _type: 是否有分类 eg: NoteStatus.Valid.value | ... 可能是一组{用字典对应}
        :return: 条数
        """

        try:
            data = {'obj': obj, 'type': _type}
            response = self.stub.GetRecordsCount(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:  # 请求失败
                raise Exception('fail to get count!')
            elif res['operation'] == ClientRequest.Success:  # 请求成功
                return res['result']
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    # 公告相关
    def GetAllNotesRequest(self, start=None, num=None, is_valid=None):
        """
        获取所有公告
        :param start:　限制田间，起始位置
        :param num:　限制条件，每页条数
        :param is_valid: 限制条件，公告过期|未过期
        :return:(...)
        """

        try:
            data = {'obj': 'note', 'start': start, 'num': num, 'is_valid': is_valid}
            response = self.stub.GetAllNotes(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:  # 请求失败
                return ()
            elif res['operation'] == ClientRequest.Success:  # 请求成功
                return res['result']
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def VoidTheNoteRequest(self, pk):
        """
        作废一则公告
        :param pk:主键　可能是一组　用字典对应
        :return:res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            data = {'note_id': pk[0]}
            response = self.stub.VoidTheNote(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to void!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def InsertANoteRequest(self, data):
        """
        添加一则新公告
        :param data:数据
        :return: res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            response = self.stub.InsertANote(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to insert!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def ModifyTheNoteRequest(self, data):
        """
        修改一则新公告
        :param data:数据
        :return: res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            response = self.stub.ModifyTheNote(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to modify!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    # 用户相关
    def GetAllUserRequest(self, start=None, num=None):
        """
        获取所有公告
        :param start:　限制田间，起始位置
        :param num:　限制条件，每页条数
        :return:
        """

        try:
            data = {'obj': 'user', 'start': start, 'num': num}
            response = self.stub.GetAllUsers(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:  # 请求失败
                return ()
            elif res['operation'] == ClientRequest.Success:  # 请求成功
                return res['result']
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def DeleteTheUserRequest(self, pk):
        """
        删除一个用户
        :param pk:主键　可能是一组　用字典对应
        :return:res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            data = {'user_id': pk[0]}
            response = self.stub.DeleteTheUser(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to delete!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def InsertAUserRequest(self, data):
        """
        添加一个新用户
        :param data:数据
        :return: res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            response = self.stub.InsertAUser(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to insert!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def ModifyTheUserRequest(self, data):
        """
        修改一则用户信息
        :param data:数据
        :return: res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            response = self.stub.ModifyTheUser(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to modify!')
            elif res['operation'] == ClientRequest.Success:
                return ClientRequest.Success
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')

    def GetSelfInfoRequest(self, data):
        """
        获取个人用户信息
        :param data:数据
        :return: res['operation'] 即ClientRequest.Sucess | ...
        """

        try:
            response = self.stub.GetTheUser(correspondence_pb2.RequestStruct(para=pickle.dumps(data)))
            res = pickle.loads(response.result)
            if res['operation'] == ClientRequest.Failure:
                raise Exception('fial to modify!')
            elif res['operation'] == ClientRequest.Success:
                return res['result'][0]
        except Exception as e:  # 界面捕捉异常并弹出警告窗口
            print(e)
            raise Exception('fail to request!')


if __name__ == '__main__':
    conn = CR()
    print conn.GetAllNotesRequest()



