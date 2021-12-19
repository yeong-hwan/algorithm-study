from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer_list = [min(matrix[i]) for i in range(N)]

print(max(answer_list))
