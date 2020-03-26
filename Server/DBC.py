# -*-coding:utf-8-*-
import pymysql


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

    def get_all_user_info(self):
        """
        获取所有用户信息
        :return: (user_info),(...
        """

        sql = 'select * from user_info;'
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


if __name__ == '__main__':
    try:
        db = DBC()
        print db.get_all_user_info()
    except Exception as e:
        print(e)
        db = None

