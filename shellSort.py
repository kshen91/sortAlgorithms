##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   shell sort
# Time Complexity:  n*log(n)
# Space Complexity: 1

def Runner(lst):

    if len(lst) == 1:
        return lst

    step = len(lst)/2
    while step != 0:
        i = 0
        while i+step < len(lst):
            for j in range(i+step, 0, -step):
                if lst[j] < lst[j-step]:
                    lst[j], lst[j-step] = lst[j-step],lst[j]
                else:
                    break
            i += step

        step /= 2

    return lst
