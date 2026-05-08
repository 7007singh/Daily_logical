def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


print(factorial(5))


# Find factorial without recursion

def fact():
    n = 5
    res = 1
    for i in range(1, n+1):
        res *= i
    print(res)

fact()