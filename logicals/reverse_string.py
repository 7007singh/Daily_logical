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
