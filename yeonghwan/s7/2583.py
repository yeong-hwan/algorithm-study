import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

# bfs
def bfs(i, j):
    count = 1
    queue.append([i, j])

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < M:

                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                    count += 1

    # print(visited)
    # print(count, "\n")
    return count


# const
M, N, K = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(K)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# print(squares)

region_areas = []

# main
visited = [[0] * M for _ in range(N)]

# 1. make wall by visit
for square in squares:
    start_x, start_y = square[0], square[1]
    end_x, end_y = square[2], square[3]

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            visited[x][y] = True

# 2. bfs counting
for j in range(M):
    for i in range(N):
        if visited[i][j] == False:
            visited[i][j] = True
            
            region_areas.append(bfs(i, j))

region_areas.sort()
print(len(region_areas))
print(*region_areas)