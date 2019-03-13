##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   insertion sort
# Time Complexity:  n ~ n^2
# Space Complexity: 1

def Runner(lst):

    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        for j in range( i, 0, -1 ):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break

    return lst
