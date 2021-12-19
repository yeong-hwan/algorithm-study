from sys import stdin
input = stdin.readline

N = int(input())
deque = []

for _ in range(N):
    cmd = input().rstrip()
    if cmd[:6] == 'push_f':
        deque.insert(0, cmd[11:])
    elif cmd[:6] == 'push_b':
        deque.append(cmd[10:])
    elif cmd == 'pop_front':
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd == 'pop_back':
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)

    elif cmd == 'size':
        print(len(deque))
    elif cmd == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    else:
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
