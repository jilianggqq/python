#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sel_sort(arr):
    l = len(arr)
    for i in xrange(0, l - 1):
        min = i
        for j in xrange(i + 1, l):
            if arr[j] < arr[min]:
                min = j
        # this change method is very well
        arr[i], arr[min] = arr[min], arr[i]
    print arr

if __name__ == '__main__':
    sel_sort([17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12])
