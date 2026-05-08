# anagram check

x = "cork"
y = "rocks"
x = sorted(x)
y = sorted(y)
if x == y:
    print(True)
else:
    print(False)



"""
Given a list of words, efficiently group all anagrams. The two strings, X and Y, are anagrams if by rearranging X's letters, we can get Y using all the original letters of X exactly once.

Input : ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']

Output:

{
    ('CARS', 'ARCS', 'SCAR'),
    ('REPAID', 'PAIRED'),
    ('SIGNED', 'DESIGN'),
    ('LANE', 'LEAN'),
    ('GRAB', 'BRAG'),
    ('NOSE', 'ONES'),
    ('DUES', 'USED', 'SUED')
}


Input : ['CARS', 'LANE', 'ONES']
Output: {}

The solution should return a set containing all the anagrams grouped together, irrespective of the order.

"""


def find_anagrams():
    lst = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    output = {}
    pairs = set()

    for i in lst:
        sorted_i = "".join(sorted(i))
        if sorted_i not in output:
            output[sorted_i]= [i]
        else:
            output[sorted_i].append(i)
    for v in output.values():
        pairs.add(tuple(v))

    print(pairs)


find_anagrams()

