from itertools import combinations
from operator import itemgetter


def import_nums(fn):
    with open(fn, 'r') as f:
        nums = [i[:-1] for i in f.readlines()]
    return nums


def after(nums, x):
    result = ''
    for i in nums:
        if x in i:
            result += i[i.index(x) + 1:]
    return len(set(result))



def calculate():
    nums = import_nums('p079_keylog.txt')
    elems = set(''.join(nums))
    result = ''
    while elems:
        for i in elems:
            temp = after(nums, i)
            if temp == len(elems) - 1:
                result += i
                elems.discard(i)
                break
    return result


print(calculate())