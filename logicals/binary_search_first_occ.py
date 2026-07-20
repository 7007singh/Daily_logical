def binary_first_occurrence():
    s = [1,3,3,3,5]
    t = 3

    left = 0
    right = len(s) - 1

    while left <= right:

        mid = (left + right) // 2

        if s[mid] == t:

            if mid == 0 or s[mid - 1] != t:
                return mid

            right = mid - 1

        elif t > s[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(binary_first_occurrence())