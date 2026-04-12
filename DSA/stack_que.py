# string = "hello"
# stack = []
# for i in string:
#     stack.append(i)
#
#
# res = ""
# while stack:
#     res += stack.pop()
# print(res)


def is_valid(s):
    s = s.replace(" ", "")
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return 0
            else:
                stack.pop()

    return True if not stack else False


print(is_valid("((()))"))

# [0, 1, 2, 3, 0, 1, 6]



# def less_money_student_count():
#     money_list = [2, 5, 7, 10, 1, 5, 11]
#     if len(money_list) == 0:
#         return
#     res = [0]
#     count = 0
#     for i in range(1, len(money_list)):
#         rest_lst = money_list[:i]
#         for j in rest_lst[::-1]:
#             if money_list[i] > j:
#                 count += 1
#             elif money_list[i] < j:
#                 break
#         res.append(count)
#         count = 0
#
#     print(res)
#
