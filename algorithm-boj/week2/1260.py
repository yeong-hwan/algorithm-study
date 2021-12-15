from sys import stdin
from collections import deque
input = stdin.readline

N, M, V = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1, N+1):
    graph[node].sort()


def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        node_now = queue.popleft()
        print(node_now, end=' ')
        for i in graph[node_now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
