# -*- coding: utf-8 -*-

from functools import reduce

# kth: index number, between 1 and len(list1)
def quick_kth(list1, kth):

    # O(n): getting min & max of list1
    f = lambda t, x: (x, t[1]) if t[0] > x else (t[0], x) if x > t[1] else t
    min, max = reduce(f, list1, (999999999999, -99999999999))

    # O(1): getting length of list1
    len1 = len(list1)

    # O(1): separating list1 as two parts
    range_size = max - min + 1
    near_kth_value = min + kth / len1 * range_size - 1
    f = lambda t, x: \
        (t[1].append(x), t[1], t[2]) if x < near_kth_value else \
        (t[2].append(x), t[1], t[2])
    _, small, big = reduce(f, list1, (None, [], []))

    x = quick_kth(small, kth1) if len(small) < kth else quick_kth(big, kth1)
    
    return min, max, near_kth_value, small, big
