import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

# bfs
def bfs(i, j, height):
    queue.append([i, j])

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:
                if field[y][x] > height and field[ny][nx] > height and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append([ny, nx])

def visit(visited, height):
    count = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True

                if field[i][j] <= height:
                    continue
                
                bfs(i, j, height)
                count += 1
    
    # print("count: ", count, "\n")
    return count


# const
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, field))

# print(field)
# print(max_height, "\n")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# main
max_safe_cnt = 1

for height in range(max_height+1):
    visited = [[0] * N for _ in range(N)]

    # ---
    # print("height:", height)
    result = visit(visited, height)
    # ---

    max_safe_cnt = max(result, max_safe_cnt)

print(max_safe_cnt)