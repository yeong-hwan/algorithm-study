from sys import stdin
input = stdin.readline

N = int(input())

triangle_list = []

for i in range(N):
    triangle_list.append(list(map(int, input().split())))
for i in range(N):
    triangle_list[i].insert(0, 0)

print(triangle_list)
