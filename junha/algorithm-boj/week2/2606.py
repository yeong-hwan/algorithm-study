import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [False]*N

adj_list = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) for x in input().split()]
    adj_list[u-1].append(v)    
    adj_list[v-1].append(u)

queue = [1]
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

print(visited.count(True)-1)