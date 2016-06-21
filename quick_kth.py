# -*- coding: utf-8 -*-

from functools import reduce


"""
Deprecated

Got inspected by Quick-Sort, an implementation by using Quick-Sort-like
and Binary-Search-like algorithm to find median from a fistful of numbers.

This implentation is deprecated because I'm too tire to spend time with its
details. It's almosts complete.

"""
def quick_median(list1):
    return quick_kth(list1, (len(list1)+1)//2)



# kth: index number, between 1 and len(list1)
def quick_kth(list1, kth):

    if len(list1) == 1:
        return list1[0], None

    if len(list1) == 2:
        return list1[0], list1[1]

    # O(n): getting min & max of list1
    min, max = find_min_and_max(list1)

    # O(1): getting length of list1
    len1 = len(list1)

    # O(1): separating list1 as two parts
    range_size = max - min + 1
    near_kth_value = min + kth / len1 * range_size - 1
    f = lambda t, x: \
        (t[1].append(x), t[1], t[2]) if x < near_kth_value else \
        (t[2].append(x), t[1], t[2])
    _, small, big = reduce(f, list1, (None, [], []))

    print(kth, near_kth_value, small, big)
    '''
    if len(small) == kth:
        if len(list1) % 2:
            return , find_min(big)
        else:
            return find_max(small), None
    else:
    '''
    a, b = quick_kth(small, kth) if kth <= len(small) else \
           quick_kth(big, kth - len(small))
    return a, b



def find_min_and_max(list1):

    f = lambda t, x: \
        (x, t[1]) if t[0] > x else \
        (t[0], x) if x > t[1] else t
    return reduce(f, list1, (99999999999999, -999999999999))



def find_max(list1):
    _, max = find_min_and_max(list1)
    return max


def find_min(list1):
    min, _ = find_min_and_max(list1)
    return min
