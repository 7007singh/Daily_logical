v = [1,-2,3,-4,5, -4,6,-7]

i = 0
pos = 0

while i < len(v):
    if v[i] < 0:
        v[pos], v[i] = v[i], v[pos]
        pos += 1

    i += 1


print(v)

v = [1, -2, 3, -4, 5]

i = 0
pos = 0

while i < len(v):
    if v[i] != 0:
        v[pos] = v[i]
        pos += 1
    i += 1

while pos < len(v):
    v[pos] = 0
    pos += 1

print(v)