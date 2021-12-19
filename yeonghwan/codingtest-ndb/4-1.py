from sys import stdin
input = stdin.readline

N = int(input())
location = [1, 1]
save_location = [1, 1]
move = list(input().split())

for direction in move:
    save_location = location[:]
    if direction == 'R':
        location[1] += 1
    elif direction == 'L':
        location[1] -= 1
    elif direction == 'U':
        location[0] -= 1
    elif direction == 'D':
        location[0] += 1
    if location[0] == 0 or location[1] == 0:
        location = save_location

print(location)
