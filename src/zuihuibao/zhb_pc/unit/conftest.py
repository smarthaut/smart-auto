#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 上午10:21
# @Author  : huanghe
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm

import pytest


@pytest.fixture()
def some_data():
    return 31