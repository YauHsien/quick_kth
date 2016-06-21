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
def seesaw_median_incre(smallD, medianD, median1D, bigD, list1O):

    small, median, median1, big, list1 = smallD, medianD, median1D, bigD, list1O

    while list1 != []:

        head = list1[0]
        tail = list1[1:]

        if small == [] and median == None and big == []:
            small, median, median1, big, list1 = small, head, median1, big, tail
        
        elif small == [] and median1 == None and big == []:
            median2, median3 = level2(median, head)
            small, median, median1, big, list1 = small, median2, median3, big, tail

        elif len(small) == len(big) and median != None and median1 != None:
            s, median, b = level(median, median1, head)
            small.append(s)
            big.append(b)
            small, median, median1, big, list1 = small, median, None, big, tail

        elif len(small) == len(big) and median != None and median1 == None:
            if head == median:
                small, median, median1, big, list1 = small, median, head, big, tail
            elif head < median:
                max_s = find_max(small)
                small.remove(max_s)
                s, median1, median2 = level(max_s, head, median)
                small.append(s)
                small, median, median1, big, list1 = small, median1, median2, big, tail
            elif median < head:
                min_b = find_min(big)
                big.remove(min_b)
                median1, median2, b = level(median, min_b, head)
                big.append(b)
                small, median, median1, big, list1 = small, median1, median2, big, tail

    return small, median, median1, big




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
