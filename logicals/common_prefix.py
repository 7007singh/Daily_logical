def longestCommonPrefix():
    strs = ["flower","flow","flight"]
    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


print(longestCommonPrefix())

