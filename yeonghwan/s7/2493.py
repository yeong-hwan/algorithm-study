import sys
from collections import deque

input = sys.stdin.readline

# const
N = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

# main
for idx in range(len(towers)):
    while stack:
        # print(idx, stack)
        if stack[-1][1] > towers[idx]: 
            result.append(stack[-1][0] + 1) # idx + 1
            break

        else:
            stack.pop()

    if not stack: 
        result.append(0)

    stack.append((idx, towers[idx])) # idx, height

print(*result)