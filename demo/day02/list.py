#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'

#新增单个数据
a = [1,2,3,4,5,6,7,8,9]
a.append(11)
print(a)
#  列表某个位置增加数据
a.insert(2,11)
print(a)
# 列表最后增加多个数据
b = [1,2,3,4]
a.extend(b)
print(a)
print(b)
print(a+b)
# 删除数据，根据下标
print(a.pop(2))
print(a)
# 根据内容删除数据
a.remove(1)
print(a)
