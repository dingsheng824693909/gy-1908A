#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'


a = 1
if(a == 3):
    print("打篮球")
else:
    print("打你mmp")



b = 70
if(b >= 80):
    print("优秀")
elif(b > 60):
    print("良好")
else:
    print("不及格")

for i in range(1,100,2):
    print(i)

# 终止
for i in range(100):
    if(i == 10):
        break
    print(i)

# 跳过
for i in range(1,100):
    if(i%2 == 0):
        continue
print(i)

v = 0
for i in range(1,101):
    v += i
print(v)

v = 1
for o in range(1,101):
    v = v * o
print(v)

# while

i = 1
while(i <= 100):
    print(i)
    i = i + 1
