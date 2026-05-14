# Check if a string is a palindrome

def palindrome():
    s = "aba"
    x = s[::-1]
    if x == s:
        return True
    else:
        return False

print(palindrome())


def find_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


print(find_palindrome("aba"))   # True
print(find_palindrome("madam")) # True
print(find_palindrome("hello")) # False