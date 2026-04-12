# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def show(self):
#         print(self.brand, self.price)
#
#
# obj = Mobile("apple", 8000)
# obj.show()
import time


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         ar = self.length * self.width
#         print("Area", ar)
#
#
# arr = Rectangle(10, 20)
# arr.area()


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def result(self):
#         if self.marks > 40:
#             print("Pass")
#         else:
#             print("Fail")
#
#
# obj = Student("Arya", 46)
# obj.result()


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")
#
#     def show_balance(self):
#         print(self.balance)
#
#
# obj = BankAccount("shweta", 1000)
# obj.deposit(500)
# obj.withdraw(100)
# obj.show_balance()


# class Vehicle:
#     def start(self):
#         print("start")
#
#
# class Bike(Vehicle):
#     def ride(self):
#         print("ride")
#
#
# obj = Bike()
# obj.start()
# obj.ride()


# class Animal:
#     def sound(self):
#         print("sound")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("meow")
#
#
# obj = Cat()
# obj.sound()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def bonus(self):
#         bonus = self.salary * 0.10
#         print(bonus)
#
#
# obj = Employee("shweta", 8000)
# obj.bonus()


# class Car:
#     def __init__(self, sound, color, brand):
#         self.sound = sound
#         self.color = color
#         self.brand = brand
#
#     def print_attribute(self):
#         print(self.sound, self.color, self.brand)
#
#
# obj = Car("sound", "blue", "bmw")
# obj.print_attribute()


# class Account:
#     def __init__(self, balance):
#         self.__balance = balance  # private
#
#     def get_balance(self):
#         return self.__balance
#
#
# obj = Account(1000)
# print(obj.get_balance())

# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def show_books(self):
#         print(self.books)
#
#
# obj = Library()
# obj.add_book("Python")
# obj.add_book("Java")
# obj.show_books()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduction(self):
#         print(f"my name is {self.name} and i am {self.age} year old")
#
#
# obj = Person("shw", 50)
# obj.introduction()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
#     def show(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Department: {self.department}")
#
#
# obj = Manager("she", 6888, "heAD")
# obj.show()

# class Test:
#     def __init__(self):
#         self.__x = 10
#
#
# t = Test()
# print(t.__x)


# def reverse_without_build_in():
#     arr = [1, 2, 3, 4]
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#     print(arr)
#
#
# reverse_without_build_in()


# def second_largest_no():
#     arr = [1, 2, 3, 4]
#     # max1 = max2 = float('-inf')
#     # for i in arr:
#     #     if i > max1:
#     #         max2 = max1
#     #         max1 = i
#     #     elif i > max2 and i != max1:
#     #         max2 = i
#     # print(max2)
#     import heapq
#     res = heapq.nlargest(3, arr)
#     print(res)
#     arr.sort(reverse=True)
#     print(arr)
#
#
# second_largest_no()


# def sum_of_sub_arr():
#     # max_sum = 0
#     # arr = [2, 1, 5, 1, 3, 2]
#     # k = 3
#     # for i in range(len(arr) - k + 1):
#     #     current_sum = sum(arr[i:i + k])
#     #     max_sum = max(max_sum, current_sum)
#     #
#     # print(max_sum)
#
#     arr = [2, 1, 5, 1, 3, 2]
#     k = 3
#
#     window_sum = sum(arr[:k])
#     max_sum = window_sum
#
#     for i in range(k, len(arr)):
#         window_sum += arr[i]  # add next element
#         window_sum -= arr[i - k]  # remove old element
#         max_sum = max(max_sum, window_sum)
#
#     print(max_sum)
#
#
# sum_of_sub_arr()


# def longest_substring():
#     s = "abcabcbb"
#
#     char_map = {}
#     left = 0
#     max_length = 0
#     for right in range(len(s)):
#         if s[right] in char_map:
#             left = max(left, char_map[s[right]] + 1)
#
#         char_map[s[right]] = right
#         max_length = max(max_length, right - left + 1)
#
#     print(max_length)
#
#
# longest_substring()


# def max_sum_of_sub_arry():
#     arr = [5,7,8,9,9,2,3,1,3,0]
#     max_sum = 0
#     window = 2
#     for i in range(len(arr) - 2):
#         arr_sum = sum(arr[i:i+window])
#         if max_sum < arr_sum:
#             max_sum = arr_sum
#
#     print(max_sum)


# def max_sum_of_sub_arry():
#     arr = [5,7,8,9,9,2,3,1,3,0]
#     window = 2
#
#     window_sum = sum(arr[:window])
#     max_sum = window_sum
#
#     for i in range(window, len(arr)):
#         window_sum += arr[i]        # add next
#         window_sum -= arr[i-window] # remove old
#
#         max_sum = max(max_sum, window_sum)
#
#     print(max_sum)
#
# max_sum_of_sub_arry()


# Smallest Subarray with Sum ≥ Target


# def smallest_arr():
#     arr = [5, 7, 2, 8, 9, 9, 2, 3, 1, 3, 0, 2]
#     target = 34
#
#     left = 0
#     current_sum = 0
#     min_length = float('inf')
#
#     for right in range(len(arr)):
#         current_sum += arr[right]
#
#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
#             current_sum -= arr[left]
#             left += 1
#
#     if min_length == float('inf'):
#         print("No subarray found")
#     else:
#         print(min_length)
#
#
# smallest_arr()


# Count Substrings with Unique Characters

# def count_unique_substrings():
#     s = "abcabc"
#
#     char_set = set()
#     left = 0
#     count = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#
#         char_set.add(s[right])
#         count += (right - left + 1)
#
#     print(count)
#
# count_unique_substrings()


# def kadane():
#     arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
#     current_sum = 0
#     max_sum = float('-inf')
#
#     for num in arr:
#         current_sum += num
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#
#         if current_sum < 0:
#             current_sum = 0
#
#     print(max_sum)
#
#
# kadane()
# def kadane():
#     arr = [-2,1,-3,4,-1,2,1,-5,4]
#
#     current_sum = max_sum = arr[0]
#
#     for i in range(1, len(arr)):
#         current_sum = max(arr[i], current_sum + arr[i])
#         max_sum = max(max_sum, current_sum)
#
#     print(max_sum)

# All negative array handle karo
#
# 🔥 Q2:
#
# Maximum product subarray


# def trap_water():
#     arr = [0,1,0,2,1,0,1,3,2,1,2,1]
#
#     left = 0
#     right = len(arr) - 1
#
#     left_max = 0
#     right_max = 0
#
#     water = 0
#
#     while left < right:
#         if arr[left] < arr[right]:
#             if arr[left] >= left_max:
#                 left_max = arr[left]
#             else:
#                 water += left_max - arr[left]
#             left += 1
#         else:
#             if arr[right] >= right_max:
#                 right_max = arr[right]
#             else:
#                 water += right_max - arr[right]
#             right -= 1
#
#     print(water)
#
# trap_water()

#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
#
# print(factorial(6))

# num = 65
#
# for i in range(1,4):
#     for j in range(i):
#         print(chr(num), end=" ")
#         num += 1
#     print()

# class MyIter:
#     def __init__(self):
#         self.x = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.x <= 3:
#             val = self.x
#             self.x += 1
#             return val
#         else:
#             raise StopIteration
#
#
# obj = MyIter()
# for i in obj:
#     print(i)

# import json
#
# with open("data.json", "r") as f:
#     data = json.load(f)
#
# print(data)


# arr = [1, 2, 3, 4]
#
# start = 0
# end = len(arr) - 1
#
# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1
#
# print(arr)

# arr = [1, 2, 3, 4]
#
# max1 = max2 = float("-inf")
#
# for i in arr:
#     if max1 < i:
#         max2 = max1
#         max1 = i
#     elif max2 < i != max1:
#         max2 = i
#
# print(max2)

# arr = [1, 2, 3, 4]
#
# left = 0
# right = len(arr) - 1
#
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
#
# print(arr)


# arr = [1, 2, 3, 4, 6]
# target = 6
#
# left = 0
# right = len(arr) - 1
#
# while left < right:
#     current_sum = arr[left] + arr[right]
#
#     if current_sum == target:
#         print("Found:", arr[left], arr[right])
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# fibonacci(5)


# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
#
#
# print(bubble_sort([5, 3, 2, 4, 1]))


# def max_subarray(arr):
#     max_current = max_global = arr[0]
#
#     for i in arr[1:]:
#         max_current = max(i, max_current + i)
#         max_global = max(max_global, max_current)
#
#     return max_global


# def merge_sort():
#     a = [1, 3, 4]
#     b = [4, 6, 9]
#     i,j= 0, 0
#     res = []
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             res.append(a[i])
#             i+=1
#         else:
#             res.append(b[j])
#             j+=1
#
#     res.extend(a[i:])
#     res.extend(b[j:])
#     print(res)
#
#
# merge_sort()


# s = "madam"
#
# left = 0
# right = len(s) - 1
#
# is_palindrome = True
#
# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1
#
# print(is_palindrome)




