# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-07 09:07:10
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/reasoning.py
# @Author : Lenovo
# @Describe : 
================================================="""

import unittest

def fun(*args) :
    print(args)
    print(type(args))
    for arg in args :
        print(arg)

def fun2(**kwargs) :
    print(kwargs)
    print(type(kwargs))
    for arg in kwargs :
        print(arg)

if __name__ == '__main__':
    t = (-1, 0, 1)
    # fun("shi", *t, 23)

    fun2(apple=1, banana=3, **{'a': 12})

import http