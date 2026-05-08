🔹 1. Basics + Logic Building (1–20)
1 Reverse a string without using slicing
2 Check if a string is a palindrome
3 Find factorial using recursion
4 Find factorial without recursion
5 Generate Fibonacci series (iterative & recursive)
6 Check if a number is prime
7 Find all prime numbers in a range
8 Swap two variables without a third variable
9 Count vowels and consonants in a string
10 Find the largest element in a list
11 Find second largest element in a list
12 Remove duplicates from a list
13 Find frequency of each element in a list
14 Find common elements between two lists
15 Check if two strings are anagrams
16 Convert string to title case without built-in functions
17 Count occurrences of a substring
18 Flatten a nested list
19 Find sum of digits of a number
20 Check Armstrong number
🔹 2. Strings & Pattern Problems (21–40)
21 Reverse words in a sentence
22 Find first non-repeating character
23 Find longest substring without repeating characters
24 Check if string contains only digits
25 Remove all special characters from a string
26 Find all permutations of a string
27 Print all substrings of a string
28 Check if two strings are rotations
29 Compress a string (e.g., "aaabb" → "a3b2")
30 Find longest palindrome substring
31 Count words in a sentence
32 Replace spaces with %20
33 Check balanced parentheses
34 Find duplicate characters in a string
35 Remove duplicate characters
36 Sort characters in a string
37 Find smallest window containing all characters of another string  - no
38 Group anagrams together
39 Check if string is subsequence of another
40 Convert Roman numeral to integer
🔹 3. Lists & Arrays Logic (41–60)
41 Rotate list by k positions
42 Find missing number in range
43 Move all zeros to end
44 Merge two sorted lists
45 Find intersection of two lists
46 Find union of two lists
47 Kadane’s Algorithm (maximum subarray sum)
48 Find pair with given sum
49 Find triplet with given sum
50 Find duplicates in list
51 Find majority element (> n/2 times)
52 Sort list without using sort()
53 Find smallest missing positive number
54 Rearrange positives and negatives alternately
55 Find subarray with given sum
56 Check if list is monotonic
Product of array except self
Find leaders in array
Longest consecutive sequence
Check if array can be divided into pairs with equal sum
🔹 4. Dictionaries & Hashing (61–70)
Count frequency using dictionary
Sort dictionary by value
Merge two dictionaries
Find key with max value
Invert a dictionary
Group elements by frequency
Check if two dictionaries are equal
Find duplicate values in dictionary
Build LRU cache logic
Count pairs with given sum using hashmap
🔹 5. Recursion & Backtracking (71–80)
Tower of Hanoi
Generate all subsets of a set
Generate all permutations of a list
Solve N-Queens problem
Sudoku solver
Word search in grid
Combination sum problem
Generate parentheses combinations
Rat in a maze
Subset sum problem
🔹 6. Object-Oriented + Pythonic Logic (81–90)
Implement a custom iterator
Implement a stack using class
Implement queue using two stacks
Singleton design pattern
Decorator to measure execution time
Create your own map() function
Create your own filter() function
Deep copy vs shallow copy implementation
Implement context manager
Implement a simple cache system
🔹 7. Advanced Logic & Real Interview Problems (91–100)
Detect cycle in linked list
Reverse a linked list
Find middle of linked list
Merge two linked lists
Implement binary search
BFS and DFS traversal
Validate binary search tree
Find lowest common ancestor
Top K frequent elements
Implement rate limiter logic


question

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