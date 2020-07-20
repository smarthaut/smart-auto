#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 下午3:01
# @Author  : huanghe
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
from utils.file_manage import ExcelReader
from utils.file_manage import YamlManage

def test_login():
    data = ExcelReader(filename='appcasedata.xlsx',sheet='pc')
