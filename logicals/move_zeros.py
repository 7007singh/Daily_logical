def move_zeroes(nums):
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums


print(move_zeroes(nums=[1,2,0,3,4,0,8,7]))