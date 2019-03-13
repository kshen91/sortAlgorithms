##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   merge sort
# Time Complexity:  n*log(n)
# Space Complexity: n

def Runner(lst):

    if len(lst) == 1:
        return lst

    while len(lst) != 1:
        list1, list2 = Runner(lst[:len(lst)/2]), Runner(lst[len(lst)/2:])
        return mergeList(list1,list2)

def mergeList(list1, list2):

    i = j = 0
    ret = []

    while i < len(list1) or j < len(list2):
        if list1[i] < list2[j]:
            ret.append(list1[i])
            i += 1
            if i == len(list1):
                ret += list2[j:]
                break
        else:
            ret.append(list2[j])
            j += 1
            if j == len(list2):
                ret += list1[i:]
                break

    return ret
