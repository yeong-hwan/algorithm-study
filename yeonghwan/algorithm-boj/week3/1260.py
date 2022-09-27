from collections import list

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(1, N+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
visited = [0] * (N+1)


def dfs(node):
    visited[node] = 1
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    queue = list([node])
    visited[node] = 1
    while queue:
        node_now = queue.popleft()
        print(node_now, end=' ')
        for i in graph[node_now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


dfs(V)
visited = [0] * (N+1)
print()
bfs(V)
