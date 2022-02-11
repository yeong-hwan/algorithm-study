from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    break_point = 0
    pop_bin = 0
    array = deque(arr[i] for i in range(len(arr)) if i % 2 == 1)

    for letter in array:
        if letter.isdigit() == False:
            print('error')
            break_point += 1
            break
    if break_point != 0:
        continue
    for cmd in p:
        if cmd == 'R':
            if pop_bin == 0:
                pop_bin = 1
            else:
                pop_bin = 0
        elif cmd == 'D':
            if pop_bin == 0:
                array.popleft()
            else:
                array.pop()
    if pop_bin == 0:
        print('[' + ','.join(array) + ']')
    else:
        array.reverse()
        print('[' + ','.join(array) + ']')
