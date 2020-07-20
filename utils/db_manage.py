#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 下午2:53
# @Author  : huanghe
# @Site    : 
# @File    : db_manage.py
# @Software: PyCharm
import pymysql

class DBManage():
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
        self.cursorclass = pymysql.cursors.DictCursor

    def connect(self):
        self.conn=pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset,cursorclass = pymysql.cursors.DictCursor)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self,sql,params=()):
        result=None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self,sql,params=()):
        list=()
        try:
            self.connect()
            self.cursor.execute(sql,params)
            list=self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list

    def insert(self,sql,params=()):
        self.__edit(sql,params)

    def update(self, sql, params=()):
        self.__edit(sql, params)

    def delete(self, sql, params=()):
        self.__edit(sql, params)

    def create(self,sql,parames=()):
        self.__edit(sql, parames)

    def __edit(self,sql,params):
        response=None
        try:
            self.connect()
            response=self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return response