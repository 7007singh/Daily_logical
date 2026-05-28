l1 = [1,2,2,2,3]
l2 = [2,3,2,6,7]
l3 = []
c_dict = {}
for i in l1:
    c_dict[i] = c_dict.get(i,0) + 1

for j in l2:
    count = c_dict.get(j,0)
    if count > 0:
        l3.append(j)
        c_dict[j] = count - 1
print(l3)