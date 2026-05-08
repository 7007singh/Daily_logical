def rev():
    num = 893
    rev_n = 0
    while num >0:
        reminder = num % 10
        rev_n = rev_n * 10 + reminder
        num = num//10
    print(rev_n)

print(rev())