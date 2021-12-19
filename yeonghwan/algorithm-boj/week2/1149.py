from sys import stdin
input = stdin.readline

N = int(input())
step_rgb_array = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(1, N):
    previous_step = step_rgb_array[i-1]
    present_step = step_rgb_array[i]
    if i == 1:
        answer.append(
            [previous_step[0], previous_step[1], previous_step[2]])

    answer.append([])

    answer[i].append(present_step[0] + min(answer[i-1][1], answer[i-1][2]))
    answer[i].append(present_step[1] + min(answer[i-1][0], answer[i-1][2]))
    answer[i].append(present_step[2] + min(answer[i-1][0], answer[i-1][1]))
print(min(answer[N-1]))
