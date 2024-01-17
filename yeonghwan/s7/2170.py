import sys
input = sys.stdin.readline

N = int(input())

lines = []

for _ in range(N):
    lines.append(tuple(map(int, input().split())))

lines.sort()

left = lines[0][0]
right = lines[0][1]
result = 0


for i in range(1, N):
    line = lines[i]
    now_left, now_right = line[0], line[1]

    if now_right <= right:
        pass

    elif now_left <= right <= now_right:
        right = now_right

    elif right < now_left:
        length = right - left
        result += length

        left = now_left
        right = now_right

length = right - left
result += length

print(result)