from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0


def dfs(x, y):
    if x >= N or x <= -1 or y >= N or y <= -1:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False


apts = 0
result = []

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(count)
            apts += 1
            count = 0

print(apts)
print(*result, sep='\n')
