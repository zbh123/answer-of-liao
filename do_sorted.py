#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


def by_name(t):
  print t
  return t[0]
def by_score(t):
  return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score)
print(L2)
L1 = sorted(L, key=by_name)
print(L1)
