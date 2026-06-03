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


def print_n(n):
    if len(n) == 0:
        return
    if n[0] != n[-1]:
        return False
    print_n(n[1:-1])
    return True


print(print_n("madam"))