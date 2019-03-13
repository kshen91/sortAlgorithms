##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   selection sort
# Time Complexity:  n^2
# Space Complexity: 1

def Runner(list):
    for i in range(len(list)):
        smallest_index = i
        for j in range(i,len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j

        list[i], list[smallest_index] = list[smallest_index], list[i]

    return list
