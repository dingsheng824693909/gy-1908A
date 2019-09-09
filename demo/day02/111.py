#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
# dergakio   要求生成两个新的字符串  drai  和egko

vv = "dergakio"
print(vv[::2])
print(vv[1::2])

# 字符串切片

a = '你好,不好,非常好'
print(a.split(","))

# 去空格
e = '                                            hasdhaso     '
print(e.rstrip())

# 替换
f = 'dsandfonsd   okfn,sdkmnf     kd,lsnal kfan'
print(f.replace(' ',''))
print(f.replace(',',''))


# GET ,https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False, HTTP/1.1
g = 'GET ,https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False, HTTP/1.1'
print(g.split(","))