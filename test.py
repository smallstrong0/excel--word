#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 上午10:34
# @Author  : SmallStrong
# @Des     : 
# @File    : test.py
# @Software: PyCharm

import sys
import core.ganjiang
import core.moye

reload(sys)
sys.setdefaultencoding('utf-8')


def go():
    dic_list = core.moye.read_data()
    core.ganjiang.write_data(dic_list)


if __name__ == '__main__':
    go()
