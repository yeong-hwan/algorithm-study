from sys import stdin
input = stdin.readline

N = int(input())

for i in range(1, N):
    print(' ' * (N-i) + '*' * (2*i - 1))

print('*' * (2*N - 1))

for i in range(1, N):
    print(' ' * i + '*' * (2*(N-i) - 1))
