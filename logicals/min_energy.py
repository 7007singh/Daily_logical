def minimumEffort():
    tasks = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
    curr = 0
    ans = 0
    for actual, minimum in tasks:
        if curr < minimum:
            ans += (minimum - curr)
            curr = minimum

        curr -= actual

    return ans

minimumEffort()