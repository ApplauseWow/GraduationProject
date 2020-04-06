# -*-coding:utf-8
# 封装rpc请求函数
from Log import log
from TypesEnum import *
from DBC import DBC


class CallMethodImplement(object):

    __operation_mapper = {
        DBOperation.Failure: ClientRequest.Failure,
        ProcessOperation.Failure: ClientRequest.Failure,
        DBOperation.Success: ClientRequest.Success,
        ProcessOperation.Success: ClientRequest.Success
    }

    __obj2table_mapper = {  # 对象映射到表
        'note': 'note_info',  # 公告
        'user': 'user_info'  # 用户
        # ...
    }


    @log
    def SayHello(self, ip, data):
        """
        用于测试
        :param ip: 用于识别客户端
        :param data:　请求参数
        :return:
        """
        d = dict()
        d['operation'] = ClientRequest.Failure
        d['exception'] = Exception('fail to ...')
        return d

    @log
    def GetRecordsCount(self, ip, data):
        """
        获取总记录条数
        :param ip: 用于识别客户端
        :param data: 请求参数
        :return: dict{'operation': , 'exception': , 'result': }
        """

        try:
            conn = DBC(client_ip=ip)
            res = conn.count_record(self.__obj2table_mapper[data['obj']], data['type'])  # _type中是字典与sql_mapper中名称必须一致
            res['operation'] = self.__operation_mapper[res['operation']]
            return res
        except Exception as e:
            return {'operation':ClientRequest.Failure, 'exception':e, 'result': None}

    @log
    def GetAllObjects(self, ip, data):
        """
        获取所有公告
        :param ip: 用于识别客户端
        :param data: 请求参数
        :return: dict{'operation': , 'exception': , 'result': }
        """

        try:
            conn = DBC(client_ip=ip)
            table = self.__obj2table_mapper[data['obj']]
            start_end = (data['start'], data['num']) if data['num'] else()
            res = conn.search_record(table=table, start_end=start_end, limitation={'is_valid': data['is_valid']})
            res['operation'] = self.__operation_mapper[res['operation']]
            return res
        except Exception as e:
            return {'operation':ClientRequest.Failure, 'exception':e, 'result': None}

    @log
    def VoidTheNote(self, ip, data):
        """
        获取所有公告
        :param ip: 用于识别客户端
        :param data: 请求参数
        :return: dict{'operation': , 'exception': , 'result': }
        """

        try:
            conn = DBC(client_ip=ip)
            data['void'] = NoteStatus.Invalid.value
            res = conn.modify_record('void', 'note_info', data)
            res['operation'] = self.__operation_mapper[res['operation']]
            return res
        except Exception as e:
            return {'operation':ClientRequest.Failure, 'exception':e, 'result': None}

