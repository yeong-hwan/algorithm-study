# from sys import stdin, setrecursionlimit
# setrecursionlimit(10 ** 6)
# input = stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
print(graph)
