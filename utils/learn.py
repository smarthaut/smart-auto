#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 上午10:30
# @Author  : huanghe
# @Site    : 
# @File    : learn.py
# @Software: PyCharm
import os


a = [str(i) for i in range(5)]
seq1 = ['hello','good','boy','doiido']

print(str(','.join(a)))

# with open('/Users/huanghe/Desktop/mem.txt','wb')as f:
#     f.write(os.system("top -l 1 | head -n 10 | grep Mem"))