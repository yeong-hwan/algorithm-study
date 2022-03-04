from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
visited = [0] * (N+1)


def bfs(node):
    queue = deque([node])
    visited[node] = 1
    while queue:
        node_now = queue.popleft()
        for i in graph[node_now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


bfs(1)
print(sum(visited)-1)
