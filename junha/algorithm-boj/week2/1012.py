from itertools import product
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    num_clusters = 0
    M, N, K = map(int, input().split())
    baechu_map = [[False]*(M+2) for _ in range(N+2)]
    for _ in range(K):
        c, r = map(int, input().split())
        baechu_map[r+1][c+1] = True

    while any(map(any, baechu_map)):
        for row, col in product(range(1, N+1), range(1, M+1)):
            if baechu_map[row][col]:
                queue = [(row, col)]
                cnt = 0
                while queue:
                    curr_house = queue.pop(0)
                    r, c = curr_house
                    if baechu_map[r][c]:
                        baechu_map[r][c] = False
                        queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
                num_clusters += 1
                break

    print(num_clusters)
