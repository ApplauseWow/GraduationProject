# -*-coding:utf-8
# 封装rpc请求函数
from Log import log
from TypesEnum import *
from DBC import DBC


class CallMethodImplement(object):

    _operation_mapper = {
        DBOperation.Failure: ClientRequest.Failure,
        ProcessOperation.Failure: ClientRequest.Failure,
        DBOperation.Success: ClientRequest.Success,
        ProcessOperation.Success: ClientRequest.Success
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
        d['operation'] = DBOperation.Failure
        d['exception'] = Exception('fail to ...')
        return d

    @log
    def GetAllNotes(self, ip, data):
        """
        获取所有公告
        :param ip: 用于识别客户端
        :param data: 请求参数
        :return: dict{'operation': , 'exception': , 'result': }
        """

        try:
            conn = DBC(client_ip=ip)
            res = conn.search_record('note_info', (data['start'], data['num']))
            res['operation'] = self._operation_mapper[res['operation']]
            if res['result']: # 如果结果不会空
                # 过滤数据
                valid_list = filter(lambda x: NoteStatus(x[4]) == NoteStatus.Valid, res['result'])  # 未过期公告
                invalid_list = filter(lambda x: NoteStatus(x[4]) == NoteStatus.Invalid, res['result'])  # 过期公告
                res['result'] = {'valid': valid_list, 'invalid': invalid_list}
            else:
                pass
            return res
        except Exception as e:
            return {'operation':ClientRequest.Failure, 'exception':e, 'result': None}

