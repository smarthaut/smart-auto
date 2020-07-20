#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 下午4:56
# @Author  : huanghe
# @Site    : 
# @File    : file_manage.py
# @Software: PyCharm
import os
import yaml
from utils.path_manage import Path
from xlrd import open_workbook,xldate_as_tuple
import xlrd
import datetime
import xlwt
from xlutils.copy import copy



class YamlManage:
    def __init__(self, filename):
        if os.path.exists(Path().get_config_path(filename)):
            self.yaml_file = Path().get_config_path(filename)
        else:
            raise FileNotFoundError("配置文件不存在")
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yaml_file,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data

    def get_data(self,element):
        print(self.data[0])
        value = self.data[0].get(element)
        print(value)
        print(self.data[0])
        return value

    def set_data(self,key,value):
        data = self.data[0]
        data[key]=value
        with open(self.yaml_file,'w') as f:
            yaml.dump(data, f, default_flow_style=False,encoding='utf-8',allow_unicode=True)

class SheetTypeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        print(self.value)


class ExcelReader:

    def __init__(self, filename,sheet=0):
        if os.path.exists(os.path.join(Path().base_path,'data',filename)):
            self.excel_file = os.path.join(Path().base_path,'data',filename)
        else:
            raise FileNotFoundError("文件不存在")
        self.sheet = sheet
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel_file)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)
            if True:
                title = s.row_values(0)  # 首行为title
                list_value = []
                num = 1
                for col in range(1, s.nrows):
                    str_obj = {}
                    for i in range(len(s.row_values(0))):
                        ctype = s.cell(num, i).ctype
                        cell = s.cell_value(num, i)
                        if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                            cell = int(cell)  # 浮点转成整型
                            cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
                        elif ctype == 3:
                            year, month, day, hour, minute, second = xldate_as_tuple(cell, 0)
                            date = datetime.datetime(year, month, day)
                            cell = datetime.datetime.strftime(date, '%F')
                        elif ctype == 4:
                            cell = True if cell == 1 else False
                        str_obj[title[i]] = cell
                    list_value.append(str_obj)
                    num = num + 1
                self._data = list_value
        return self._data


class ExcelWriter:

    def __init__(self,filename,sheet_name):
        if os.path.exists(os.path.join(Path().base_path,'result',filename)):
            self.workbook = xlrd.open_workbook(os.path.join(Path().base_path,'result',filename))
            if sheet_name in self.workbook.sheet_names():
                worksheet = self.workbook.sheet_by_name(sheet_name)  # 获取工作簿中所有表格中的的第一个表格
                self.rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
                self.work_book = copy(self.workbook)  # 将xlrd对象拷贝转化为xlwt对象
                self.work_sheet = self.work_book.get_sheet(sheet_name)  # 获取转化后工作簿中的第一个表格
            else:
                self.rows_old = 0
                self.work_book = copy(self.workbook)
                self.work_sheet = self.work_book.add_sheet(sheet_name)
        else:
            self.rows_old = 0
            self.work_book = xlwt.Workbook()
            self.work_sheet = self.work_book.add_sheet(sheet_name)  # 在工作簿中新建一个表格
        self.filename = filename


    def write_file(self,value):
        index = len(value)  # 获取需要写入数据的行数
        for i in range(0, index):
            for j in range(0, len(value[i])):
                self.work_sheet.write(i+self.rows_old, j, value[i][j])  # 像表格中写入数据（对应的行和列）
        path = os.path.join(Path().base_path, 'result', self.filename)
        self.work_book.save(path)


if __name__  == '__main__':
    yml_data = YamlManage('config.yml')
    print(yml_data.get_data('name'))

    # data = ExcelWriter(filename='aaa.xlsx',sheet_name='2')
    # data.write_file([[1,2,3]])
