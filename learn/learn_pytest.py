#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 下午1:44
# @Author  : huanghe
# @Site    : 
# @File    : learn_pytest.py
# @Software: PyCharm
from collections import namedtuple
Task = namedtuple('Task',['summer','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2
