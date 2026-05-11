def separateDigits():
    nums = [13, 25, 83, 77]
    output = []
    for i in nums:
        for j in str(i):
            output.append(int(j))
    return [int(digit) for num in nums for digit in str(num)]


print(separateDigits())
