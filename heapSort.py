##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

# sort algorithm:   heap sort
# Time Complexity:  n*log(n)
# Space Complexity: 1

# class Node(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def Runner(lst):

    ret = []
    # convert the list into a heap (BST)
    # for each node index from floor(n/2) ~ 0, make sure the root val is the largest
    while len(lst) >= 1:
        for i in range(len(lst)/2, 0, -1):
            # node = Node(lst[i-1])
            # node.left = Node(lst[2*i-1])
            # if 2*i < len(lst):
            #     node.right = Node(lst[2*i])

            # sortNode(node)
            if 2*i < len(lst): #node has a right child
                if lst[2*i-1] > lst[i-1] and lst[2*i-1] >= lst[2*i]:
                    lst[i-1],lst[2*i-1] = lst[2*i-1], lst[i-1]
                elif lst[2*i] > lst[i-1] and lst[2*i] > lst[2*i-1]:
                    lst[i-1],lst[2*i] = lst[2*i],lst[i-1]

            else: #node only has a left child
                if lst[2*i-1] > lst[i-1]:
                    lst[i-1],lst[2*i-1] = lst[2*i-1],lst[i-1]

        # swap index 0 and the last one in the BST, and remove last one from the tree
        lst[0], lst[-1] = lst[-1], lst[0]
        ret = [lst.pop()] + ret

    return ret
