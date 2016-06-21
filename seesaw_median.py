# -*- coding: utf-8 -*-

from quick_kth import find_min, find_max



"""
Seesaw Strategy Median Finding Algorithm:

With O(n) complexity, using an incremental strategy to find median
between three parts of numbers.

Return: A structure with four elements, "small, median, median1, big,"
including a list with numbers smaller than or equal to the median, one or
two numbers as the median, and a list with rest numbers.

"""
def seesaw_median(list1):
    small = []
    big = []
    median = None
    median1 = None
    return seesaw_median_incre(small, median, median1, big, list1)





"""
Seesaw Strategy Median Finding Algorithm: with Incremental Technique
"""
def seesaw_median_incre(small, median, median1, big, list1):

    if list1 == []:
        return small, median, median1, big

    head = list1[0]
    tail = list1[1:]

    if small == [] and median == None and big == []:
        return seesaw_median_incre(small, head, median1, big, tail)

    if small == [] and median1 == None and big == []:
        median2, median3 = level2(median, head)
        return seesaw_median_incre(small, median2, median3, big, tail)

    if len(small) == len(big) and median != None and median1 != None:
        s, median, b = level(median, median1, head)
        small.append(s)
        big.append(b)
        return seesaw_median_incre(small, median, None, big, tail)

    if len(small) == len(big) and median != None and median1 == None:
       if head == median:
           return seesaw_median_incre(small, median, head, big, tail)
       if head < median:
           max_s = find_max(small)
           small.remove(max_s)
           s, median1, median2 = level(max_s, head, median)
           small.append(s)
           return seesaw_median_incre(small, median1, median2, big, tail)
       if median < head:
           min_b = find_min(big)
           big.remove(min_b)
           median1, median2, b = level(median, min_b, head)
           big.append(b)
           return seesaw_median_incre(small, median1, median2, big, tail)
        
    return None # Problem occurs here.




# level(a, b) returns a1, b1 where a1 < b1 or a1 = b1
def level2(a, b):
    if a > b:
        return b, a
    return a, b



# : return a1 <= b1 <= c1
def level(a, b, c):
    a1, b1 = level2(a, b)
    b2, c1 = level2(b1, c)
    a2, b3 = level2(a1, b2)
    return a2, b3, c1
