#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 下午9:00
# @Author  : SmallStrong
# @Des     : ganjiang is a tool of write data to word
# @File    : ganjiang.py
# @Software: PyCharm

import sys
import docxtpl

reload(sys)
sys.setdefaultencoding('utf-8')


def write_data(dic_list):
    for data in dic_list:
        doc = docxtpl.DocxTemplate("word_test.docx")
        doc.render(data)
        doc.save("./export/{}.docx".format(data['placeholder_1']))
