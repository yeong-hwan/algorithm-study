from sys import stdin
from collections import deque
input = stdin.readline

node_count = int(input())
edge_count = int(input())
visited = [False] * (node_count+1)
graph = [[] for _ in range(node_count+1)]

for _ in range(edge_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1, node_count+1):
    graph[node].sort()


def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


dfs(1)

print(visited.count(True)-1)
