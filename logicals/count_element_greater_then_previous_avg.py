""""Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

Example

Input

responseTimes = [100, 200, 150,300]
Output

2"""


def find_element_grater_then_previous_avg():
    x = [100, 200, 150,300]
    count = 0
    for i in range(1, len(x)):
        avg = sum(x[:i]) / i
        if avg < x[i]:
            count += 1
    print(count)


find_element_grater_then_previous_avg()
