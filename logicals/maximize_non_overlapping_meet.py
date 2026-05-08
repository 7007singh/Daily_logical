def maximizeNonOverlappingMeetings(meetings):
    if len(meetings) == 0:
        return 0
    meetings.sort(key=lambda x: x[1])
    count = 1
    end_time = meetings[0][1]
    for i, v in meetings[1:]:
        if end_time <= i:
            count += 1
            end_time = v
    return len(meetings) - count


print(maximizeNonOverlappingMeetings([[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]]))

