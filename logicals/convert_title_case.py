# convert to title case

x = "very map APPLE good"
y = x.split()
res = []
for i in y:
    first_char = i[0].upper()
    rest_char = i[1:].lower()
    res.append(first_char + rest_char)
r = " ".join(res)
print(r)
