from collections import list
N, M, V = map(int, input().split())
visited = [0] * 1001
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i in range(1, N+1):
    nodes[i].sort()
print(nodes[:10])


def dfs(node):
    visited[node] = 1
    print(node, end=' ')
    for node_now in nodes[node]:
        if not visited[node_now]:
            dfs(node_now)


def bfs(node):
    queue = list([node])
    visited[node] = 1
    while queue:
        node_now = queue.popleft()
        print(node_now, end=' ')
        for i in nodes[node_now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


dfs(V)
visited = [0] * 1001
print()
bfs(V)
