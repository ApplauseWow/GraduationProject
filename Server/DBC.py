# -*-coding:utf-8-*-
import pymysql
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from TypesEnum import *


class DBC(object):
    """
    数据库交互
    """

    def __init__(self, client_ip):
        tree = ET.parse("./ClientMapper.xml")  # 解析数据库信息xml
        root = tree.getroot()  # 获取根节点
        client_info = dict()  # 客户端映射信息
        res = filter(lambda x: x.get('c_ip') == client_ip, root.findall('client'))  # 查找对应客户端信息
        if res == []:  # 未查到对应的客户端信息
            raise Exception("No such a client info!")
        else:  # 已查到
            for pair in res[0].items():
                client_info[pair[0]] = pair[1]
        try:
            self.conn = pymysql.connect(host=client_info['host'],
                                        user=client_info['user'],
                                        db=client_info['db'],
                                        port=int(client_info['port']),
                                        password=client_info['pwd'],
                                        charset='utf8',
                                        connect_timeout = 5
                                        )
        except Exception as e:
            self.conn = None
            raise Exception("fail to connect to the DB!")

    def close_connect(self):
        """
        关闭数据库连接
        :return:None
        """

        if self.conn:
            self.conn.close()
        else:
            pass

    def get_all_info(self, table, start_end = ()):
        """
        获取表所有信息
        :return: (info),(...
        """

        if start_end is ():  # 不需要分页
            sql = "select * from %s;" % table
        else:  # 需要分页
            sql = "select * from %s limit %s, %s;" % (table, start_end[0], start_end[1])
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            users = cursor.fetchall()
        except Exception as e:
            print(e)
            users = None
        finally:
            cursor.close()
        return users  # 返回None为出错 ()为没有记录

    # user_info表
    def insert_record(self, table, para_dict=None):
        """
        添加新记录
        :param table: 表
        :param para_dict: 数据字典
        :return:DBOperation().
        """

        sql = ""
        cursor = self.conn.cursor()
        try:
            row = cursor.execute(sql,( 9, 9, 9, 0, None, '163'))
            if row == 1:  # 插入成功
                self.conn.commit()  # 必须提交事务才能生效
                return DBOperation.Success
            else:  # 插入失败
                return DBOperation.Failure
        except Exception as e:  # 插入失败
            print(e)
            return DBOperation.Failure
        finally:
            cursor.close()


if __name__ == '__main__':
    try:
        db = DBC('192.168.2.104')
        a = db.get_all_info("user_info", (0, 3))
        print len(a)
        print(a == ())
        for i in a:
            print(i)
        # b = db.insert_user()
        # print(b)
    except Exception as e:
        print(e)
        db = None



