from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1) if len(queue) == 0 else print(0)
    elif command[0] == "front":
        print(queue[0]) if len(queue) != 0 else print(-1)
    elif command[0] == "back":
        print(queue[-1]) if len(queue) != 0 else print(-1)
