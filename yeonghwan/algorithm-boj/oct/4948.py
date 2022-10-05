import math
import sys
input = sys.stdin.readline


N = 123456*2 + 1
is_prime = [True] * N

for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, N, i):
            is_prime[j] = False

while True:
    num = int(input())

    if num == 0:
        break
    cnt = 0

    for i in range(num+1, 2*num + 1):
        if is_prime[i]:
            cnt += 1

    print(cnt)
