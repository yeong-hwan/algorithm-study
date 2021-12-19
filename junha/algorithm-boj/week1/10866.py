from sys import stdin 

N = int(input())

deque = [] 
for _ in range(N):
    user_input = stdin.readline()
    user_command = user_input.split()[0]
    
    if user_command == 'push_front':
        x = int(user_input.split()[1])
        deque.insert(0, x)

    elif user_command == 'push_back':
        x = int(user_input.split()[1])
        deque.append(x)

    elif user_command == 'pop_front':
        print(-1 if len(deque) == 0 else deque.pop(0))

    elif user_command == 'pop_back':
        print(-1 if len(deque) == 0 else deque.pop())

    elif user_command == 'size':
        print(len(deque))

    elif user_command == 'empty':
        print(1 if len(deque) == 0 else 0)

    elif user_command == 'front':
        print(-1 if len(deque) == 0 else deque[0])

    elif user_command == 'back':
        print(-1 if len(deque) == 0 else deque[-1])

    else:
        raise NotImplementedError