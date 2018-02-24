#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 上午10:27
# @Author  : SmallStrong
# @Des     : moye is a tool to read the excel data
# @File    : moye.py
# @Software: PyCharm
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import xlrd


def read_data():
    data = xlrd.open_workbook('excel_test.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows
    # ncols = table.ncols
    dic_list = []
    for i in range(nrows):
        _list = table.row_values(i)
        dic = {}
        for i in range(len(_list)):
            dic['placeholder_{}'.format(i + 1)] = _list[i]
        dic_list.append(dic)
    return dic_list
