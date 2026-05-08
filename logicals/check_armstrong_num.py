# Check Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


print(is_armstrong(153))  # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))  # False


def find_armstrong(start, end):
    return [n for n in range(start, end + 1) if is_armstrong(n)]


print(find_armstrong(1, 10000))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
