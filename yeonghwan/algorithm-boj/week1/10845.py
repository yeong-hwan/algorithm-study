from sys import stdin
input = stdin.readline

N = int(input())
queue = []

for _ in range(N):
    cmd = input().rstrip()
    if len(cmd) > 5:
        queue.append(cmd[5:])
    elif cmd == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
