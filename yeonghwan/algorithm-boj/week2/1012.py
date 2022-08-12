from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

T = int(input())


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for case in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1

    print(result)
