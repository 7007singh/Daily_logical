# first non repeating character
s = "my name is shweta"
for i in range(len(s)-1):
    if i == " ":
        continue
    if s[i] in s[i+1:]:
        continue
    print(s[i])
    break

from collections import Counter


def first_unique(s):
    freq = Counter(s)

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return ch

    return -1
s = "leetcode"
print(first_unique(s))

