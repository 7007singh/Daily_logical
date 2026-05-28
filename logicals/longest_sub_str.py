# longest sub string without repeating character

s = "shwetasinghabcdefghijkl"
# b = []
# r = ""
#
# for i in s:
#     r += i
#     if len(set(r)) == len(r):
#         continue
#     else:
#         r = r[:-1]
#         b.append(r)
#         r = i
#
# b.append(r)
# print(max(b, key=len))


def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


length_of_longest_substring()
