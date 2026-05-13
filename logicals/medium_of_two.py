def find_medium():
    nums1 = [1, 2]
    nums2 = [3, 4]
    arr = sorted(nums1 + nums2)
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


print(find_medium())
