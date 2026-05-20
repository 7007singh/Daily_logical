from collections import Counter


def top_k(nums, k):
    freq = Counter(nums)
    return [x[0] for x in freq.most_common(k)]


nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 6, 6]
print(top_k(nums, 4))
