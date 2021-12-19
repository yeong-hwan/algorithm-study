from sys import stdin 

N = int(input())

queue = [] 
for _ in range(N):
    user_input = stdin.readline()
    user_command = user_input.split()[0]
    
    if user_command == 'push':
        x = int(user_input.split()[1])
        queue.append(x)

    elif user_command == 'pop':
        print(-1 if len(queue) == 0 else queue.pop(0))

    elif user_command == 'size':
        print(len(queue))

    elif user_command == 'empty':
        print(1 if len(queue) == 0 else 0)

    elif user_command == 'front':
        print(-1 if len(queue) == 0 else queue[0])

    elif user_command == 'back':
        print(-1 if len(queue) == 0 else queue[-1])

    else:
        raise NotImplementedError