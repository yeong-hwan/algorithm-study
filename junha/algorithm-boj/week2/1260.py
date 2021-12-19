N, M, V = [int(x) for x in input().split()] 

adj_list = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) for x in input().split()]
    adj_list[u-1].append(v)    
    adj_list[v-1].append(u)

# DFS
stack = [V]
visited = [False]*N
result = []

while stack:
    visiting = stack.pop()
    if visited[visiting-1]:
        pass
    else:
        result.append(visiting)
        visited[visiting-1] = True
        stack.extend(sorted(adj_list[visiting-1], reverse=True))

print(*result, sep=' ')

# BFS
queue = [V]
visited = [False]*N
result = []

while queue:
    visiting = queue.pop(0)
    if visited[visiting-1]:
        pass
    else:
        result.append(visiting)
        visited[visiting-1] = True
        queue.extend(sorted(adj_list[visiting-1]))

print(*result, sep=' ')