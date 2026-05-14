def reverse_string():
    s = "shweta"
    r = ""
    for i in s:
        r = i + r
    return r


print(reverse_string())

s = "pyrhon"
rev = "".join(reversed(s))
print(rev)

from functools import reduce

rre = reduce(lambda x, y: y + x, s)
print(rre)


from collections import Counter

s = "banana"

print(Counter(s))

nums = [1,2,3,5]

n = 5

expected = n * (n + 1) // 2
actual = sum(nums)

print(expected - actual)
