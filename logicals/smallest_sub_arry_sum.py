def max_sum_subarray():

    arr = [1,2,3,4,5,3,2,1,3]
    k = 3

    current_sum = sum(arr[:k])
    max_sum = current_sum
    left = 0
    right = k
    while right < len(arr):
        current_sum = current_sum - arr[left] + arr[right]
        if current_sum > max_sum:
            max_sum = current_sum
        left += 1
        right += 1

    return max_sum


print(max_sum_subarray())