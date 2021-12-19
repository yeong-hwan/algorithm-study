from sys import stdin
input = stdin.readline

N = int(input())
stack = []

for _ in range(N):
    cmd = input().rstrip()
    if len(cmd) > 5:
        stack.append(cmd[5:])
    elif cmd == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
