#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def normalize(name):
  name_norm = ''
  for i l in enumerate(name):
    if i == 0:
      name_norm = name_norm + l.upper()   #变大写
    else :
      name_norm = name_norm + l.lower()   #变小写
 return name_normal
 
 def normalize1(name):
  name_norm = []
  for i in name:
    name_norm.append(i.capitalize())     #将首字母大写，其余小写
 return name_normal
 
 L1 = ['adam','LISA','barT']
 L2 = list(map(normalize,L1))            #normalize和normalize1效果一样
 L3 = normalize(L1)
 
 
 
