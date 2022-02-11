from collections import deque

queue = deque()
K = int(input())

for _ in range(K):
    now = int(input())
    if now == 0:
        queue.pop()
    else:
        queue.append(now)

print(sum(queue))
