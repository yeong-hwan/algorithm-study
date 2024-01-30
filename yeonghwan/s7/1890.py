import sys
from collections import deque

input = sys.stdin.readline


# const
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

x, y = 0, 0
distance = board[x][y]

while True:
    