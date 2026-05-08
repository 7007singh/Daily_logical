#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling function, {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"completed")
#         return result
#     return wrapper
#
#
# @logger
# def add(a,b):
#     x = a + b
#     print(x)
#
#
# add(7,9)


# class Countdown:
#     def __init__(self, start):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         val = self.current
#         self.current -= 1
#         return val
#
#
# for n in Countdown(5):
#     print(n)  # 5, 4, 3, 2, 1


import threading
from multiprocessing import Process

def print_no():
    for i in range(5):
        print(f"thread: {i}")


# t = threading.Thread(target=print_no())
# t.start()
# t.join()


t = Process(target=print_no())
t.start()
t.join()

# import threading
#
# balance = 1000
# lock = threading.Lock()
#
# def withdraw(amount):
#     global balance
#     with lock:                    # only one thread enters at a time
#         if balance >= amount:
#             balance -= amount
#             print(f"Withdrew {amount}, balance: {balance}")
#         else:
#             print(f"Not enough balance! Have {balance}, need {amount}")
#
# t1 = threading.Thread(target=withdraw, args=(500,))
# t2 = threading.Thread(target=withdraw, args=(700,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print(balance)  # always 500, never -200 ✅
