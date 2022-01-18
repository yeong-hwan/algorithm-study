from sys import stdin
input = stdin.readline

T = int(input())


def fib(N):
    a, b = 1, 1
    if N <= 2:
        print(1)
    else:
        for _ in range(N-2):
            a = b
            b = a+b
        print(b)


for i in range(T):
    N = int(input())
    fib(N)


# graph = [list(map(int, input().split())) for _ in range(N)]
# queue = deque()
# dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
# start_list = []


# for x in range(N):
#     for y in range(M):
#         if graph[x][y] == 1:
#             start_list.append((x, y))
# for start_point in start_list:
#     queue.append((start_point[0], start_point[1]))


# def bfs():
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M:
#                 if graph[nx][ny] == 0:
#                     graph[nx][ny] = graph[x][y] + 1
#                     queue.append((nx, ny))


# bfs()
# answer = 0
# for x in range(N):
#     for y in range(M):
#         if graph[x][y] == 0:
#             print(-1)
#             exit(0)
#     answer = max(answer, max(graph[x]))
# print(answer-1)
