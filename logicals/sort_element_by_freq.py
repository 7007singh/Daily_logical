"""Given an integer array, in-place sort its element by their frequency and index. If two elements have different frequencies,
then the one which has more frequency should come first; otherwise, the one which has less index should come first, i.e.,
the solution should preserve the relative order of the equal frequency elements.

Input : [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
Output: [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]"""


def arrange_frequency_wise():
    lst = [3, 1, 3, 1, 1, 1, 9, 8, 3, 3, 3, 3, 6, 8, 7, 8, 7]

    freq = {}
    first_index = {}

    # Count frequency and store first index
    for i, v in enumerate(lst):
        freq[v] = freq.get(v, 0) + 1
        if v not in first_index:
            first_index[v] = i

    # Sort by frequency and first index
    lst.sort(key=lambda x: (-freq[x], first_index[x]))

    return lst


print(arrange_frequency_wise())
