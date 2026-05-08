# Count occurrences of a substring

s = "abababa"
b = "aba"
count = 0
i = 0
while i <= len(s) - len(b):
    a = s[i:i + len(b)]
    if a == b:
        count += 1
        i += len(b)
    else:
        i += 1
print(count)

count = 0

for i in range(len(s) - len(b) + 1):
    x = s[i:i + len(b)]
    if x == b:
        count += 1
print(count)


# Print all substrings of a string

def print_all_substring():
    s = "alaabskdj"
    all_sub = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            all_sub.add(s[i:j])
    print(all_sub)


print_all_substring()


# def longest_superb_substring():
#     s = "lkkaahs"
#     char_set = set()
#     left = 0
#     max_length = 0
#
#     for right in range(len(s)):
#         # If duplicate, shrink window
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)
#
#     return max_length


# output
# print(longest_superb_substring())


def longest_superb_substring():
    s = "lkkaahs"
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_superb_substring())
