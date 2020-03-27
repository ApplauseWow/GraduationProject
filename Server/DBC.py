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
        return users  # 返回None为出错 ()为没有记录

    # user_info表
    def insert_user(self, user_info_dict=None):
        """
        添加新用户
        :param user_info_dict:
        :return:DBOperation().
        """

        sql = "INSERT INTO `user_info` (`user_id`, `grade`, `_class`, `user_type`, `tel`, `email`) " \
                                        "VALUES (%s, %s, %s, %s, %s, %s);"
        cursor = self.conn.cursor()
        try:
            row = cursor.execute(sql,( 9, 9, 9, 0, None, '163'))
            if row == 1:
                self.conn.commit()  # 必须提交事务才能生效
                return DBOperation.Success
            else:
                return DBOperation.Failure
        except Exception as e:
            print(e)
            return DBOperation.Failure
        finally:
            cursor.close()


'''
DELETE FROM `user_info` WHERE `user_id`='201610414206';
INSERT INTO `user_info` (`user_id`, `grade`, `_class`, `user_type`, `tel`, `email`) VALUES ('12', '21', '21', '2', NULL, NULL);


'''


if __name__ == '__main__':
    try:
        db = DBC()
        a = db.get_all_info('user_info', (0, 3))
        print len(a)
        print(a == ())
        for i in a:
            print(i)
        # b = db.insert_user()
        # print(b)
    except Exception as e:
        print(e)
        db = None


