from sys import stdin
input = stdin.readline

N = int(input())
number_sets = [int(number) for number in input().split()]
print(max(number_sets), min(number_sets))
