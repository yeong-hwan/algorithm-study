from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    # num_doc, check_loaction
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    index = [0 for _ in range(N)]
    index[M] = 1
    count = 0

    while queue:
        if queue[0] == max(queue):
            count += 1
            if index[0] == 1:
                print(count)
                break
            queue.pop(0)
            index.pop(0)
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))
