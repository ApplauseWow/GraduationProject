# -*-coding:utf-8-*-
import pymysql
from TypesEnum import *


class DBC(object):
    """
    数据库交互
    """

    def __init__(self):
        try:
            self.conn = pymysql.connect(host = '118.89.37.200',
                                        user = 'gpdb_user',
                                        db = 'gpdb',
                                        port = 3306,
                                        password='123qwe',
                                        charset = 'utf8',
                                        connect_timeout = 5
                                        )
        except Exception as e:
            raise Exception("fail to connect!")
            self.conn = None

    def close_connect(self):
        """
        关闭连接
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

        if start_end is ():
            sql = 'select * from {};'.format(table)
        else:
            sql = 'select * from {} limit {}, {}'.format(table, start_end[0], start_end[1])
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            users = cursor.fetchall()
        except Exception as e:
            print(e)
            users = None
        finally:
            cursor.close()
        return users

    # user_info表
    def insert_user(self, user_info_dict):
        """
        添加新用户
        :param user_info_dict:
        :return:DBOperation().
        """

        sql = "DELETE FROM `user_info` WHERE `user_id`='201610414206';"



if __name__ == '__main__':
    try:
        db = DBC()
        a = db.get_all_info('user_info', (0, 3))
        for i in a:
            print i[4] == None
    except Exception as e:
        print(e)
        db = None

