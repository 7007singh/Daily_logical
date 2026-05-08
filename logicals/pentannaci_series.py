def pentanacci(n):
    # given starting values
    p = [0, 1, 2, 3, 4]

    if n < 5:
        return p[n]

    for i in range(5, n + 1):
        next_val = sum(p)
        p.pop(0)
        p.append(next_val)
    print(p)
    return p[-1]



n = 10
print(pentanacci(n))