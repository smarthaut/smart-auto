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

    # 获取文件的绝对路径
    # dirname :父目录  filename:文件名
    def get_real_path(self, dirname, filename):
        return os.path.join(self.base_path, dirname, filename)

    #获取配置文件的绝对路径
    def get_config_path(self, filename):
        return os.path.join(self.base_path,'config',filename)

    #获取xml文件
    def get_xml_path(self,filename):
        return os.path.join(self.base_path, 'data/xml', filename)



if __name__ == '__main__':
    path = Path()
    print(path.get_xml_path('上海——上海.xml'))