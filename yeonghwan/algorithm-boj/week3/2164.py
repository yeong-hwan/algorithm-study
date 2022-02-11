from collections import deque

queue = deque()
N = int(input())

for i in range(N):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue[0])
