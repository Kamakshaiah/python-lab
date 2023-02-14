# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:05:11 2023

@author: GIM
"""

def argsDemo(*args):
    for arg in args:
        print(arg)
        
argsDemo(1, 2, 3, 4)
argsDemo('m', 'k')

def kwargsDemo(**kwargs):
    for kw in kwargs:
        print(kw, kwargs[kw])
        
kwargsDemo(name='mk', age=47)

## applications

def summaryStatsitics(x, *args):
    import statistics
    if 'am' in args:
        print(statistics.mean(x))
    if 'gm' in args:
        print(statistics.geometric_mean(x))
    if 'hm' in args:
        print(statistics.harmonic_mean(x))
        
summaryStatsitics(range(10), 'am')
summaryStatsitics(range(1, 11), 'gm')
summaryStatsitics(range(1, 11), 'hm')

