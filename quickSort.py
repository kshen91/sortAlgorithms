##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   quick sort
# Time Complexity:  n*log(n) ~ n^2
# Space Complexity: log(n)

def Runner(lst):
    return partition(lst) # just keep this function name, Runner() is used to run test case

def partition(lst):

    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    smaller = []
    greater = []

    for i in range(len(lst)-1):
        if lst[i] > pivot:
            greater.append(lst[i])
        else:
            smaller.append(lst[i])

    return (partition(smaller) + [pivot] + partition(greater))
