def find_duplicate_in_list():
    x = [1,3,4,5,6,3,4,5]
    y = list(set(x))
    for item in y:
        if item in x:
            x.remove(item)
    return x

print(find_duplicate_in_list())


def find_duplicates(lst):
    seen = set()
    dup = set()
    for i in lst:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
    return list(dup)