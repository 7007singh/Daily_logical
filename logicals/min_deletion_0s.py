def min_deletions(s):
    # find first and last '1'
    first = s.find('1')
    last = s.rfind('1')

    # if no '1' or only one '1'
    if first == -1 or first == last:
        return 0

    # count zeros between them
    count = 0
    for i in range(first, last + 1):
        if s[i] == '0':
            count += 1

    return count


s = "00100101010111"
print(min_deletions(s))



