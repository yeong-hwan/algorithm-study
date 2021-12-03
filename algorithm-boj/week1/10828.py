from sys import stdin 

N = int(input())

stack = [] 
for _ in range(N):
    user_input = stdin.readline()
    user_command = user_input.split()[0]
    
    if user_command == 'push':
        x = int(user_input.split()[1])
        stack.append(x)

    elif user_command == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())

    elif user_command == 'size':
        print(len(stack))

    elif user_command == 'empty':
        print(1 if len(stack) == 0 else 0)

    elif user_command == 'top':
        print(-1 if len(stack) == 0 else stack[-1])

    else:
        raise NotImplementedError