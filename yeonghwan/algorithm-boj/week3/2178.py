from collections import deque
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    print(graph[N-1][M-1])


bfs(0, 0)
