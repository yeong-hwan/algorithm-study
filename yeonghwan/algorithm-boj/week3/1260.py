from collections import deque
N, M, V = map(int, input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1, N+1):
    graph[node].sort()


def dfs(node):
    visited[node] = 1
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    visited[node] = 1
    while queue:
        node_now = queue.popleft()
        print(node_now, end=' ')
        for i in graph[node_now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


dfs(V)
print()
visited = [0] * (N+1)
bfs(V)
