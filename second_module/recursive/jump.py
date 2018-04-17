# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'yangyang'
__mtime__ = '2017.12.29'
"""
s = "a string to examine"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            answer = (i, j)
            print(answer)
            break