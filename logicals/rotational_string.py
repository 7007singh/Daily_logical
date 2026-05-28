# Check if two strings are rotations

s = "abx"
b = "xba"
if len(s) != len(b):
    print(False)
if b in s + s:
    print(True)

