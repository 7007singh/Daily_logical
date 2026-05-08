"""
Given an unsorted integer array, find all triplets in it with sum less than or equal to a given number.

Input : nums[] = [2, 7, 4, 9, 5, 1, 3], target = 10
Output: {(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5)}

Input : nums[] = [3, 5, 7, 3, 2, 1], target = 5
Output: {}

Since the input can have multiple triplets with sum less than or equal to the target, the solution should return a set
containing all the distinct triplets in any order.
"""


def find_triplets():
    lst = [2, 7, 4, 9, 5, 1, 3]
    n = len(lst)
    target = 10
    output = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(i + 2, n):
                x = lst[i] + lst[j] + lst[k]
                if x <= target:
                    output.add(tuple(sorted((lst[i], lst[j], lst[k]))))
    print(output)


find_triplets()
