from sys import stdin
input = stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif command[0] == "top":
        print(stack[-1]) if len(stack) != 0 else print(-1)
