def min_move():
    nums = [37, 2, 9, 49, 58, 57, 48, 17]
    limit = 58
    n = len(nums)

    # difference array
    diff = [0] * (2 * limit + 2)

    # process each pair
    for i in range(n // 2):
        a = nums[i]
        b = nums[n - 1 - i]

        low = min(a, b) + 1
        high = max(a, b) + limit
        s = a + b

        # initially assume 2 moves for all sums
        diff[2] += 2
        diff[2 * limit + 1] -= 2

        # reduce to 1 move for range [low, high]
        diff[low] -= 1
        diff[high + 1] += 1

        # reduce to 0 move for exact sum s
        diff[s] -= 1
        diff[s + 1] += 1

    # prefix sum to compute actual costs
    ans = float('inf')
    curr = 0

    for target in range(2, 2 * limit + 1):
        curr += diff[target]
        ans = min(ans, curr)

    return ans


print(min_move())
