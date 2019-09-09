#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'

a ={}
a1 = {'name':'哦哦哦','sex':'哦'}
print(a1)
a1['age']=8
print(a1)
# 删除字典
print(a1.pop('age'))
print(a1)

#del a1['sex']
#print(a1)

#del a1
#print(a1)
# 清空
# a1.clear()
# print(a1)

# 字典合并
b1 = {'name':'牛娃','sex':'18'}
b2 = {'22':'33','44':'55'}
b1.update(b2)
print(b1)

b3 = dict(b1,**b2)
print(b3)