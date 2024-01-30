import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(i, j):
    count = 1
    queue.append([i, j])

    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 0:
                    continue

                if field[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(visited[nx][ny], count)
                    queue.append([nx, ny])
                    
    return count-1

# const
N, M = map(int, input().split())
field = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if field[i][j] == "L":
            field[i][j] = 1
        else:
            field[i][j] = 0

# main
result=0

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            result = max(result, bfs(i, j))

print(result)