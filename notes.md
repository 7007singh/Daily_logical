s = [[1, 2], [3, 4]]
print(id(s[0]))

s[0] = s[0] + [99]
print(id(s[0]))   # 🔄 different

s = [[1, 2], [3, 4]]
print(id(s[0]))

s[0] += [99]
print(id(s[0]))   # ✅ same


+ → "build a new list and replace it"
+= → "edit the existing list"


# Case 1
s[0] = s[0] + [99]   # NEW list → shallow NOT affected

# Case 2
s[0] += [99]         # SAME list modified → shallow affected


sorted("python")       # ['h', 'n', 'o', 'p', 't', 'y']
sorted((3, 1, 2))      # [1, 2, 3]  ← tuple input
sorted({3, 1, 2})      # [1, 2, 3]  ← set input
sorted({'b':2, 'a':1}) # ['a', 'b'] ← dict keys

lst = ['banana', 'apple', 'kiwi']

lst.sort(key=len, reverse=True)         # in-place
print(lst)                              # ['banana', 'apple', 'kiwi']

print(sorted(lst, key=len, reverse=True))  # new list