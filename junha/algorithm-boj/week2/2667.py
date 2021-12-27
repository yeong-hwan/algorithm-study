from itertools import product
from sys import stdin
input = stdin.readline

N = int(input())
house_map = [
    [False]*(N+2),
    *[[False, *[x == '1' for x in input().strip()], False] for _ in range(N)],
    [False]*(N+2),
]
num_clusters = []

while any(map(any, house_map)):
    for row, col in product(range(1, N+1), range(1, N+1)):
        if house_map[row][col]:
            queue = [(row, col)]
            cnt = 0
            while queue:
                curr_house = queue.pop(0)
                r, c = curr_house
                if house_map[r][c]:
                    cnt += 1
                    house_map[r][c] = False
                    queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
            num_clusters.append(cnt)
            break

print(len(num_clusters))
print(*sorted(num_clusters), sep="\n")
