from sys import stdin
input = stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    if N < 4:
        print(1)
    elif N < 6:
        print(2)
    else:
        a, b, c, d, e = 1, 1, 1, 2, 2
        for i in range(6, N+1):
            a, b, c, d, e = b, c, d, e, e+a
        print(e)
