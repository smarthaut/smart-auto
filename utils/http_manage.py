#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 上午9:23
# @Author  : huanghe
# @Site    : 
# @File    : http_manage.py
# @Software: PyCharm
import requests
import json
from utils.log_manage import Logger

class BaseHttp:

    def __init__(self, method, host, timeout=60):
        self.method = method
        self.host = host
        self.timeout = timeout
        self.url = ""
        self.headers = {}
        self.params = {}
        self.cookies = ""
        self.data = {}
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()

    def set_url(self, url):
        self.url = self.host + url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_cookies(self, cookies):
        self.cookies = cookies

    def set_data(self,data):
        self.data = data

    def get_post(self,jsontype=1):
        try:
            response = None
            if self.method in ["get","GET"]:
                response = requests.get(self.url, headers=self.headers, params=self.params,
                                        timeout=float(self.timeout), cookies=self.cookies)
            elif self.method in ["post","POST"]:
                if jsontype == 0:
                    response = requests.post(self.url, headers=self.headers,data=self.data,
                                  timeout=float(self.timeout), cookies=self.cookies)
                else:
                    response = requests.post(self.url, headers=self.headers, json=json.dumps(self.data),
                                             timeout=float(self.timeout), cookies=self.cookies)
            self.logger.info("请求接口为: {}".format(self.url))
            self.logger.info("响应状态码为：{}".format(response.status_code))
            self.logger.info("响应内容为：{}".format(response.text))
            return response
        except Exception as e:
            print('未进行容错处理的情况：', e)
            return None

if __name__ == '__main__':
    basehttp = BaseHttp(method='get', host='http://172.17.2.75:5000')
    basehttp.set_url("/get-cookies")
    response = basehttp.get_post()
    # response01 = requests.get("http://172.17.2.75:5000/get-cookies")
    # print(response)
    print(response)
