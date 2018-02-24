#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 下午9:00
# @Author  : SmallStrong
# @Des     : 
# @File    : ganjiang.py
# @Software: PyCharm

import sys
import docxtpl

reload(sys)
sys.setdefaultencoding('utf-8')


def go():
    doc = docxtpl.DocxTemplate("./my_word_template.docx")
    context = {
        'placeholder_1': "small strong",
        'placeholder_2': "小泽",
        'placeholder_3': "玛利亚",
        'placeholder_4': "老师",
        'placeholder_5': "fanfan",
        'placeholder_6': "DW",
        'placeholder_7': "wo wo wo",
        'placeholder_8': "十块钱",
        'placeholder_9': "新年好",
        'placeholder_10': "918",
        'placeholder_11': "大佬好",
        'placeholder_12': "南京南京",
        'placeholder_13': "Hello World",
    }
    doc.render(context)
    doc.save("./export/generated_doc.docx")


if __name__ == '__main__':
    go()
