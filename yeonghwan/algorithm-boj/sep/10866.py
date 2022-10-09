from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())

deque = deque()

for _ in range(N):
    cmd = list(map(str, input().split()))
    order = cmd[0]

    if order == "push_front":
        deque.appendleft(cmd[1])
    elif order == "push_back":
        deque.append(cmd[1])
    elif order == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif order == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        print(-1) if len(deque) == 0 else print(deque[0])
    elif order == "back":
        print(-1) if len(deque) == 0 else print(deque[-1])
