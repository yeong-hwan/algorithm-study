from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

first = num_list[-1]
second = num_list[-2]

print((M // (K+1)) * (K*first + second) + (M % (K+1)) * first)
