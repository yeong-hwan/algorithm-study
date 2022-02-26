N = int(input())
ans = []
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings = sorted(meetings, key=lambda x: x[0])
meetings = sorted(meetings, key=lambda x: x[1])

meetings = meetings[::-1]

while meetings:
    meeting_now = meetings.pop()
    start = meeting_now[0]
    end = meeting_now[1]
    if not ans:
        ans.append(meeting_now)
    elif ans[-1][1] <= start:
        ans.append(meeting_now)

print(len(ans))
