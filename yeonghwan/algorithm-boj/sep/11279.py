import heapq
from sys import stdin
input = stdin.readline

N = int(input())
heap = []

for _ in range(N):
    order = int(input())
    if order == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-order, order))
