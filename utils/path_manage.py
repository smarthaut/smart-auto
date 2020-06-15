#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 下午4:58
# @Author  : huanghe
# @Site    : 
# @File    : path_manage.py
# @Software: PyCharm
import os


class Path:
    def __init__(self):
        self.base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        
    def get_config_path(self, filename):
        return os.path.join(self.base_path,'config',filename)



if __name__ == '__main__':
    path = Path()
    print(path.get_config_path('aaa.txt'))