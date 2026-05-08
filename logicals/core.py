# def info(**data):
#     for key, value in data.items():
#         print(key, ":", value)
#
#
# info(name="Rahul", age=21)
#
#
# def print_num_n(n):
#     if n == 0:
#         return
#     print_num_n(n - 1)
#     print(n)
#
#
# print(print_num_n(5))
#
#
# def sum_of_num(n):
#     if n == 0:
#         return 0
#     return n + sum_of_num(n - 1)
#
#
# print(sum_of_num(5))
#
#
# # # Swap two variables without a third variable
# a = 4
# b = 7
# b = a + b
# a = b - a
# b = b - a
# print(a,b)
#
#
# s = "my name is shweta"
# x = s.split()
# r = []
# for i in x:
#     word = i[::-1]
#     r.append(word)
# res = " ".join(r)
# print(res)


s = "SDFSAG"
print(s[:-1])