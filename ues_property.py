#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999

class Screen(object) :
    @property
    def width(self) :
        return self._width

    @width.setter
    def width(self,valuer) :
        if not isinstance(valuer,int):
            raise ValueError('score must be an integer')
        if valuer < 0 :
            raise ValueError('score must over zero')    
        self._width=valuer

    @property
    def height(self) :
        return self._height

    @height.setter
    def height(self,number) :
        if not isinstance(number,int) :
            raise ValueError('score must be an integer')
        if number < 0 :
            raise ValueError('score must be an zero')
        self._height = number

    @property
    def resolution(self):
        return self._width * self._height

s=Screen()
s.width = 1024
s.height = 768
print(s.resolution) 

