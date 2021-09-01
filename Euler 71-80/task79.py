from itertools import combinations
from time import time
from typing import List


def import_nums(fn: str) -> List[str]:
    with open(fn, 'r') as f:
        nums = set(i[:-1] for i in f.readlines())
    return list(nums)


def number_in_result(number: str, result: str) -> bool:
    for i in range(len(number)):
        if number[i] in result:
            result = result[result.index(number[i]) + 1:]
        else:
            return False

    return True


def calculate() -> str:
    nums: List[str] = import_nums('Euler 71-80//p079_keylog.txt')
    result: str = nums.pop(0)

    while len(nums) != 0:
        index: int = 0

        while index < len(nums):
            temp_number = nums[index]

            if number_in_result(temp_number, result):
                nums.pop(index)
                continue

            if temp_number[1] == result[-1]:
                result += temp_number[2]
                index += 1
                continue

            if temp_number[0] in result and temp_number[2] in result \
                and (index_start := result.index(temp_number[0])) + 1 == (index_end := result.index(temp_number[2])):
                result = result[:index_start + 1] + temp_number[1] + result[index_end:]
                nums.pop(index)
                continue

            index += 1

    return result


if __name__ == "__main__":
    start = time()
    print(calculate())
    print(f"Time: {time() - start}")
