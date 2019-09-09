#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'

# 无参数，无返回值方法
def jia():
    a = 3
    b = 5
    print(a+b)

jia()

# 有参数，无返回值

def jia(a,b):
    print(a+b)

jia(2,3)

# 无参数，有返回值
def jia():
    a = 3
    b = 5
    return a+b

c =jia()
print(c)

# 有参数，有返回值
def jia(a,b):
    return a+b

c =jia(3,6)
print(c)

def xx(a,b=9):
    return a+b
print(xx(110))
print(xx(110,10))


class ClassDemo():
    def aaa(self):
        print("xxx")
    def bbb(self):
        print("lll")
        self.aaa()
    c = ClassDemo()
    c.aaa()
    c.bbb()
