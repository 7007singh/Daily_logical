"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Input: nums = [3,2,4], target = 6
Output: [1,2]"""


# def return_target_indices():
#     nums = [5,5,8, 2, 4]
#     target = 10
#     for i in nums:
#         x = target - i
#         if x in nums and x != i:
#             return [nums.index(x), nums.index(i)]
#
#
# print(return_target_indices())


def twoSum() :
    nums = [5,5,8, 2, 4]
    target = 10
    seen = {}
    for i, num in enumerate(nums):
        complete = target - num
        if complete in seen:
            return [seen[complete],i]
        else:
            seen[complete] = i

print(twoSum())

# space comlaxity = O(n)
# time comlaxity = O(n)

