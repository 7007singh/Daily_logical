# first non repeating character
s = "my name is shweta"
for i in range(len(s)-1):
    if i == " ":
        continue
    if s[i] in s[i+1:]:
        continue
    print(s[i])
    break

