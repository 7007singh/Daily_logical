def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        count += (1 if num == candidate else -1)

    return candidate

print(majority_element([1,2,3,4,3,2,1,4,3,2]))