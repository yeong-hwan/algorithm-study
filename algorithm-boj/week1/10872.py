from sys import stdin
input = stdin.readline

N = int(input())

if N == 0:
    print(1)
else:
    answer = N
    for i in range(N-1, 1, -1):
        answer *= i
    print(answer)
