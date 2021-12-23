# from sys import stdin
# input = stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


complex_count = 0
apartment_count = []
count = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            apartment_count.append(count)
            complex_count += 1
            count = 0

print(complex_count)
apartment_count.sort()
print(*apartment_count, sep='\n')
