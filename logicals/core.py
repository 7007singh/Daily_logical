def sub_string():
    x = "alsdkjfajadldr"
    l = 0

    left = 1
    right = 0

    while left < len(x):
        if x[left] in x[right:left]:
            right = left
        a = left - right + 1
        if a > l:
            l = a
        left += 1
    return l
print(sub_string())



