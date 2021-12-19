from sys import stdin
input = stdin.readline

start_point = input()
row = ord(start_point[0])-96
column = int(start_point[1])
location = [row, column]
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]
answer = 0

for step in steps:
    x = location[0] + step[0]
    y = location[1] + step[1]
    if 0 < x < 9 and 0 < y < 9:
        answer += 1

print(answer)
