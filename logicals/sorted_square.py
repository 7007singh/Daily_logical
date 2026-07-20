def sorted_squares(arr):
    n = len(arr)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result


print(sorted_squares([-4,-1,0,3,10]))