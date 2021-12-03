from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

queue = [i for i in range(1, N+1)]
