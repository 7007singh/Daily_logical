# Generate Fibonacci series (iterative & recursive)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(1000))


# def fibonacci_iterative():
#     a = 0
#     b = 1
#     n = 5
#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#
#
# fibonacci_iterative()
