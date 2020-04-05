# -*-coding:utf-8-*-
# 用于各种小测试
from TypesEnum import *


if __name__ == '__main__':

    class Out:
        def __init__(self):
            self.i = self.Inner()
            print(id(self.i), id(self.Inner()))

        class Inner:
            def __init__(self):
                self.i()

            def i(self):
                print("inner finc")

    o = Out()
    print(id(o))
    o.__init__()
    print(id(o))