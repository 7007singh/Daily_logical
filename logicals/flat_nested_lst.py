def flat_nested_list(lst):
    flat_list = []

    for i in lst:
        if isinstance(i, list):
            flat_list.extend(flat_nested_list(i))
        else:
            flat_list.append(i)
    return flat_list


l = [1, [2, [3, 4], 5], [6, 7], 8]

print(flat_nested_list(l))
