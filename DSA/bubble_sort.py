def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [5, 2, 9, 1, 5, 6]
print(bubble_sort(lst))


def sort_string(s):
    lst = list(s)
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return ''.join(lst)


print(sort_string("python"))  # 'hnopty'