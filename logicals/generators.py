def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibo()

for _ in range(5):
    print(next(gen))



