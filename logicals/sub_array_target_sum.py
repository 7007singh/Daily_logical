
def target_sum():
    arr = [1, 2, 3, 4, 5, 3, 3, 2, 1, 3]
    target = 6

    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum >= target:

            window_length = right - left + 1
            min_length = min(min_length, window_length)

            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


print(target_sum())