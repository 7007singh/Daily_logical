# def merge_sorted(l1, l2):
#     i = j = 0
#     result = []
#     while i < len(l1) and j < len(l2):
#         if l1[i] < l2[j]:
#             result.append(l1[i])
#             i += 1
#         else:
#             result.append(l2[j])
#             j += 1
#     result.extend(l1[i:])
#     result.extend(l2[j:])
#     return result
#
# l1 = [1,2,35,7]
# l2 = [5,6,78]
#
# print(merge_sorted(l1,l2))

# merge two sorted list in ascending order


a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = 0
j = 0

result = []

while i < len(a) and j < len(b):

    if a[i] < b[j]:
        result.append(a[i])
        i += 1

    else:
        result.append(b[j])
        j += 1


# remaining elements from a
while i < len(a):
    result.append(a[i])
    i += 1


# remaining elements from b
while j < len(b): 
    result.append(b[j])
    j += 1


print(result)
