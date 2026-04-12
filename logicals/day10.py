"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Input: nums = [3,2,4], target = 6
Output: [1,2]"""

# def return_target_indices():
#     nums = [8, 2, 4]
#     target = 10
#     for i in nums:
#         x = target - i
#         if x in nums and x != i:
#             return [nums.index(x), nums.index(i)]
#
#
# print(return_target_indices())


"""Mubashir needs your help to find out number of animals hidden in a given string txt.

You are provided with an array of animals given below:

animals = ["dog", "cat", "bat", "cock", "cow", "pig",
"fox", "ant", "bird", "lion", "wolf", "deer", "bear",
"frog", "hen", "mole", "duck", "goat"]
Rule: Return the maximum number of animal names. See the below example:

txt = "goatcode"

count_animals(txt) ➞ 2
First animal = "dog"
Remaining string = "atcoe",
Second animal = "cat".
count = 2 (correct)

If you got a "goat" first time
remaining string = "code",
no animal will be found during next time.
count = 1 (wrong)
Examples
count_animals("goatcode") ➞ 2
"dog", "cat"

count_animals("cockdogwdufrbir") ➞ 4
"cow", "duck", "frog", "bird"

count_animals("dogdogdogdogdog") ➞ 5
"""

"""
Given an unsorted integer array, find all triplets in it with sum less than or equal to a given number.

Input : nums[] = [2, 7, 4, 9, 5, 1, 3], target = 10
Output: {(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5)}

Input : nums[] = [3, 5, 7, 3, 2, 1], target = 5
Output: {}

Since the input can have multiple triplets with sum less than or equal to the target, the solution should return a set
containing all the distinct triplets in any order.
"""

# def find_triplets():
#     nums = [2, 7, 4, 9, 5, 1, 3]
#     target = 10
#     res = set()
#     n = len(nums)
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(i+2, n):
#                 x = nums[i] + nums[j] + nums[k]
#                 if x <= target:
#                     triplet = tuple(sorted((nums[i], nums[j], nums[k])))
#                     res.add(triplet)
#     return res
#
#
# print(find_triplets())


"""
Given a list of words, efficiently group all anagrams. The two strings, X and Y, are anagrams if by rearranging X's letters, we can get Y using all the original letters of X exactly once.

Input : ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']

Output:

{
    ('CARS', 'ARCS', 'SCAR'),
    ('REPAID', 'PAIRED'),
    ('SIGNED', 'DESIGN'),
    ('LANE', 'LEAN'),
    ('GRAB', 'BRAG'),
    ('NOSE', 'ONES'),
    ('DUES', 'USED', 'SUED')
}


Input : ['CARS', 'LANE', 'ONES']
Output: {}

The solution should return a set containing all the anagrams grouped together, irrespective of the order.

"""

#
# def find_anagrams():
#     lst = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED',
#            'LEAN', 'SCAR', 'DESIGN']
#
#     anagram_map = {}
#
#     for word in lst:
#         # Sort the characters to create a "key"
#         # 'CARS' -> 'ACRS'
#         sorted_word = "".join(sorted(word))
#
#         if sorted_word not in anagram_map:
#             anagram_map[sorted_word] = [word]
#         else:
#             anagram_map[sorted_word].append(word)
#
#     # Filter out groups that only have one word (no anagrams found)
#     return [tuple(group) for group in anagram_map.values() if len(group) > 1]
#
#
# print(find_anagrams())


"""Given an integer array, in-place sort its element by their frequency and index. If two elements have different frequencies, 
then the one which has more frequency should come first; otherwise, the one which has less index should come first, i.e., 
the solution should preserve the relative order of the equal frequency elements.

Input : [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
Output: [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]"""

# def arrange_frequency_wise():
#     lst = [3, 1, 3, 1, 1, 1, 9, 8, 3, 3, 3, 3, 6, 8, 7, 8, 7]
#
#     freq = {}
#     first_index = {}
#
#     # Count frequency and store first index
#     for i, v in enumerate(lst):
#         freq[v] = freq.get(v, 0) + 1
#         if v not in first_index:
#             first_index[v] = i
#
#     # Sort by frequency and first index
#     lst.sort(key=lambda x: (-freq[x], first_index[x]))
#
#     return lst
#
#
# print(arrange_frequency_wise())


""""
Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False if it doesn't.

Examples
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
Notes
Only check for diagonals, horizontals and verticals.

"""

# def bingo_check(board):
#     n = 5
#
#     # Check rows
#     for row in board:
#         if all(cell == "x" for cell in row):
#             return True
#
#     # Check columns
#     for col in range(n):
#         if all(board[row][col] == "x" for row in range(n)):
#             return True
#
#     # Check main diagonal
#     if all(board[i][i] == "x" for i in range(n)):
#         return True
#
#     # Check secondary diagonal
#     if all(board[i][n - 1 - i] == "x" for i in range(n)):
#         return True
#
#     return False
#
#
# print(bingo_check([
#     [67, 43, 31, 74, "x"],
#     [64, "x", 47, "x", 90],
#     [37, 65, "x", 83, 54],
#     [67, "x", 39, "x", 44],
#     ["x", 59, 24, 30, "x"]
# ]))


""""Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

Example

Input

responseTimes = [100, 200, 150,300]
Output

2"""


# def countResponseTimeRegressions(responseTimes):
#     count = 0
#     total = 0
#
#     for i, v in enumerate(responseTimes):
#         if i > 0:
#             avg = total / i
#             if v > avg:
#                 count += 1
#         total += v
#
#     return count
#
#
# if __name__ == '__main__':
#     responseTimes_count = int(input().strip())
#
#     responseTimes = []
#
#     for _ in range(responseTimes_count):
#         responseTimes_item = int(input().strip())
#         responseTimes.append(responseTimes_item)
#
#     result = countResponseTimeRegressions(responseTimes)
#
#     print(result)


# def findSmallestMissingPositive(orderNumbers):
#     unique_no = set(orderNumbers)
#     i = 1
#     while i in unique_no:
#         i += 1
#     return i
#
#
# if __name__ == '__main__':
#     orderNumbers_count = int(input().strip())
#
#     orderNumbers = []
#
#     for _ in range(orderNumbers_count):
#         orderNumbers_item = int(input().strip())
#         orderNumbers.append(orderNumbers_item)
#
#     result = findSmallestMissingPositive(orderNumbers)
#
#     print(result)

# def isAlphabeticPalindrome(code):
#     alpha_str = ""
#     for i in code:
#         x = i.isalpha()
#         if x:
#             alpha_str += i
#     low_str = alpha_str.lower()
#     reverse_str = low_str[::-1]
#     if reverse_str == low_str:
#         return True
#     return False
#
# print(isAlphabeticPalindrome("A1b2B!a"))

#
# def isNonTrivialRotation(s1, s2):
#     # Write your code here
#     if s1 != s2:
#         temp = s1 + s2
#         if s2 in temp:
#             return True
#         return False
#     return False
#
#
# print(isNonTrivialRotation("a", "b"))


# def binarySearch(nums, target):
#     # Write your code here
#     for i, v in enumerate(nums):
#         if v == target:
#             return i
#         else:
#             return -1
#
#
# if __name__ == '__main__':
#     nums_count = int(input().strip())
#
#     nums = []
#
#     for _ in range(nums_count):
#         nums_item = int(input().strip())
#         nums.append(nums_item)
#
#     target = int(input().strip())
#
#     result = binarySearch(nums, target)
#
#     print(result)


# def maximizeNonOverlappingMeetings(meetings):
#     if len(meetings) == 0:
#         return 0
#     meetings.sort(key=lambda x: x[1])
#     count = 1
#     end_time = meetings[0][1]
#     for i, v in meetings[1:]:
#         if end_time <= i:
#             count += 1
#             end_time = v
#     return len(meetings) - count
#
#
# print(maximizeNonOverlappingMeetings([[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]]))

#
# def validate_brackets(snippet):
#     pairs = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#     code_snp = snippet.replace(" ", "")
#     for i in code_snp:
#         print(i)
#
#
# snippet = "if (a[0] > b[1]) { doSomething(); }"
# validate_brackets(snippet)



def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split(" ")
    rev_words = []
    for word in words:
        rev_word = ""
        for w in word:
            if w.isupper():
                w = w.lower()
            else:
                w = w.upper()
            rev_word += w
        rev_words.append(rev_word)
    rev_sentence = " ".join(rev_words[::-1])
    print(rev_sentence)
    return rev_sentence

reverse_words_order_and_swap_cases("aWESOME is cODING")