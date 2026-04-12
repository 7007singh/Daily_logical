n = 5

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()


for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(chr(65+j), end="")
    for j in range(i-2, -1, -1):
        print(chr(65+j), end="")
    print()


""" *
   ***
  *****
   ***
    *
"""


for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(chr(65+j), end="")
    for j in range(i-2,-1,-1):
        print(chr(65+j), end="")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print(chr(65+j), end="")
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n or i == j:
            print("*", end="")
        else:
            print(" ", end="")

    print()

for i in range(1, n+1):
    for j in range(1, i+1):
        if i == 1 or i == n or j == i or j == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()





