def longestCommonPrefix(arr1, arr2):
    prefixes = set()

    for a in arr1:
        while a > 0:
            if a in prefixes:
                break
            prefixes.add(a)
            a //= 10

    r = 0

    for b in arr2:
        while b > r:
            if b in prefixes:
                r = b
                break
            b //= 10

    return len(str(r)) if r else 0


arr1 = [1, 10, 100]
arr2 = [1000]

print(longestCommonPrefix(arr1, arr2))



