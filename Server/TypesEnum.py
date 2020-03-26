# -*-coding:utf-8-*-
from enum import Enum
from enum import unique


@unique
class UserType(Enum):
    """
    用户类型枚举类
    """

    Student = 0

    Teacher = 1