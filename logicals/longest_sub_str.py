# longest sub string without repeating character

s = "shwetasinghabcdefghijkl"
b = []
r = ""

for i in s:
    r += i
    if len(set(r)) == len(r):
        continue
    else:
        r = r[:-1]
        b.append(r)
        r = i

b.append(r)
print(max(b, key=len))
