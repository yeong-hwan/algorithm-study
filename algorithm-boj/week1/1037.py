from sys import stdin
input = stdin.readline

count = int(input())
divisor_list = [int(divisor) for divisor in input().split()]

print(max(divisor_list) * min(divisor_list))
