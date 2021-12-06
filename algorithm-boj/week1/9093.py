# from sys import stdin
# input = stdin.readline

count = int(input())

for _ in range(count):
    words = input().split()
    for word in words:
        print(word[::-1], end=' ')
