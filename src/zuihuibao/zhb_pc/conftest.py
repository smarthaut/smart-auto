#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 上午10:18
# @Author  : huanghe
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import pytest
from utils.file_manage import YamlManage
from utils.file_manage import ExcelReader


@pytest.fixture()
def some_data():
    return 32


@pytest.fixture()
def set_up_data():
    yaml_reader = YamlManage('config.yml')
    name = yaml_reader.get_data('name')
    print(yaml_reader)
    yield name
    yaml_reader.set_data('name',213)


# @pytest.fixture()
def gen_data():
    excel_reader = ExcelReader('appcasedata.xlsx',sheet='pc')
    values = []
    for data in excel_reader.data:
        value = tuple([value for value in data.values()])
        values.append(value)
    return values











