






# def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#     freq = {}
#     for i in range(minSize, maxSize+1):
#         for j in range(len(s)-i+1):
#             sub_string = s[j:j+i]
#             unique_char = len(set(sub_string))
#             if unique_char > maxLetters:
#                 continue
#             if sub_string not in freq:
#                 freq[sub_string] = 1
#             else:
#                 freq[sub_string] += 1
#     if not freq:
#         return 0
#     v = max(freq, key=freq.get)
#     print(freq)
#
#     return freq[v]
#
# print(maxFreq("abcdef", 2,3,3))


# # check if string contain only digits
#
# s = '8873490'
# for i in s:
#     if i.isdigit():
#         continue
#     else:
#         print("no only digit")

# # remove all special character form sting

# s = "Hello@123#World!"
# result = ""
#
# for ch in s:
#     if ch.isalnum():
#         result += ch
#
# print(result)

# Find all permutations of a string


# def permute(s, current=""):
#     if len(s) == 0:
#         print(current)
#         return
#
#     for i in range(len(s)):
#         remaining = s[:i] + s[i + 1:]
#         permute(remaining, current + s[i])
#
#
# # Example usage
# permute("ABC")






# compress a string

def compress_string():
    a = "aaabb"
    r = ""
    b = {}
    for i in a:
        if i in b:
            b[i] = b.get(i) + 1
        else:
            b[i] = 1
    for i, v in b.items():
        r += i
        r += str(v)
    print(r)
compress_string()


def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def find_duplicates(s):
    freq = {}
    duplicates = []

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch, count in freq.items():
        if count > 1:
            duplicates.append(ch)

    return duplicates


def remove_duplicates(s):
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)

# def sort_string(s):
#     return "".join(sorted(s))

# Find the smallest window containing all characters of another string

# group anagrams together

# def group_anagrams(words):
#     groups = {}
#
#     for word in words:
#         key = "".join(sorted(word))
#
#         if key in groups:
#             groups[key].append(word)
#         else:
#             groups[key] = [word]
#
#     return list(groups.values())
#
#
# # Example
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(words))

# Check if string is subsequence of another

s = "abc"
x = "alkdbsc"
