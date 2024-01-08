import sys
from collections import deque

input = sys.stdin.readline

# def dfs(graph, start_node):
#     not_visited = deque()
#     visited = []
#     friend_count = 0

#     not_visited.append(start_node)

#     while not_visited:
#         node = not_visited.pop()

#         if node not in visited:
#             visited.append(node)
#             not_visited.extend(graph[node])

#             friend_count += 1

#         print(node, friend_count)

#     return visited


def dfs(start_node, friend_count):
    global answer

    visited[start_node] = True
    

    if friend_count == 5:
        answer = 1
        return
    
    for idx in graph[start_node]:
        if visited[idx] == False:
            dfs(idx, friend_count + 1)
    
    visited[start_node] = False


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    f, t = map(int, input().split())
    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)
    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f)

answer = 0
visited = [False] * N

for start_node in range(N):
    dfs(start_node, 1)
    if answer:
        break

print(answer)

