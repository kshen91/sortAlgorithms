##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   bubble sort
# Time Complexity:  n ~ n^2
# Space Complexity: 1

def Runner(list):

    notFinishFlag = True

    while notFinishFlag:
        notFinishFlag = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                #as long as a swap happened, loop one more time
                notFinishFlag = True

    return list
