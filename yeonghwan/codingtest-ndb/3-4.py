from sys import stdin
input = stdin.readline

i = 0
N, K = map(int, input().split())

while N >= 1:
    if N == 1:
        print(i)
        break
    elif N % K == 0:
        N = N // K
    else:
        N -= 1
    i += 1
