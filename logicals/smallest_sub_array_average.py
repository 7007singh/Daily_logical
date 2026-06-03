def max_sum_subarray():

    arr = [1,2,3,4,5,3,2,1,3]
    k = 3

    current_sum = sum(arr[:k])
    arr_sum_avg = [current_sum//k]
    left = 0
    right = k
    while right < len(arr):
        current_sum = current_sum - arr[left] + arr[right]
        arr_sum_avg.append(current_sum//k)
        left += 1
        right += 1

    return arr_sum_avg


print(max_sum_subarray())