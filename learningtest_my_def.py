# -*- coding=utf-8 -*-

def my_abs(x):
    if not isinstance(x,(int,float)):
        return 'TypeErro:out of given'
    if x>=0:
        return x
    else:
        return -x

