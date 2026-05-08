
# 🟢 LEVEL 1
# ✅ 1. Print 1–10
def print_1_to_10(n):
    if n == 0:
        return
    print_1_to_10(n-1)
    print(n)

print_1_to_10(10)


# ✅ 2. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# ✅ 3. Sum of numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))


# 🟡 LEVEL 2
# ✅ 4. Fibonacci (Recursion)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(6):
    print(fib(i), end=" ")



# ✅ 5. Power (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2, 4))  # 16


# ✅ 6. Reverse String
def reverse_str(s):
    if s == "":
        return ""
    return reverse_str(s[1:]) + s[0]

print(reverse_str("hello"))


# 🟠 LEVEL 3
# ✅ 7. Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))  # 6


# ✅ 8. Count digits
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(1234))  # 4

# 👉 ⚠️ Edge case:
#
# if n == 0:
#     return 1



# ✅ 9. Palindrome check
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))



# 🔴 LEVEL 4 (Advanced 🔥)
# ✅ 10. Flatten List
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4], 5]]))



# ✅ 11. Tower of Hanoi
def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, helper, source, destination)

hanoi(3, 'A', 'B', 'C')


# ✅ 12. Nested Dictionary Print
def print_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print(key, ":")
            print_dict(value)
        else:
            print(key, ":", value)

data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}

print_dict(data)