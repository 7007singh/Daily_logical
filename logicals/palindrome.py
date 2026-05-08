# Check if a string is a palindrome

def palindrome():
    s = "aba"
    x = s[::-1]
    if x == s:
        return True
    else:
        return False

print(palindrome())