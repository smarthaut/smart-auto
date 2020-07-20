#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 下午1:43
# @Author  : huanghe
# @Site    : 
# @File    : test_yml_manage.py
# @Software: PyCharm
import pytest
from src.zuihuibao.zhb_pc.conftest import gen_data
from utils.file_manage import YamlManage


@pytest.mark.smoke
def test_get():
    yml_data = YamlManage('config.yml')
    user = yml_data.get_data('ZPA').get('user')
    expected = 17621100841
    assert user == expected


@pytest.mark.set
@pytest.mark.smoke
def test_set():
    yml_data = YamlManage('config.yml')
    yml_data.set_data('name','张三')
    yml_data = YamlManage('config.yml')
    name = yml_data.get_data('name')
    expected = '张三'
    assert name == expected


# @pytest.mark.xfail()
@pytest.mark.parametrize('a, b', [(1, 2), (3, 4),(5, 6)])
def test_add(a,b):
    a = a
    b = b
    result = a + b
    assert 3 == result


data = [(2, 1), (3, 1), (4, 2)]
@pytest.mark.sub
@pytest.mark.parametrize('a,b', data, ids=['{}'.format(a)for a in data])
def test_sub(a, b):
    result = a-b
    assert 2 == result


@pytest.mark.equal
def test_equal(some_data):
    assert some_data == 31



@pytest.mark.data
def test_name(set_up_data):
    assert '张三' == set_up_data

values = gen_data()
@pytest.mark.demo
@pytest.mark.parametrize('id,projectname,purpose,casename,url,method,params,assert_func', values)
def test_base_data(id,projectname,purpose,casename,url,method,params,assert_func):
    assert id == projectname






