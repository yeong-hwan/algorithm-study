from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    # num_doc, check_loaction
    N, M = map(int, input().split())
    # desc
    queue_importance = list(map(int, input().split()))
    queue, i = [], 1
    for importance in queue_importance:
        queue.append((i, importance))
        i += 1
    queue.sort(key=lambda x: (-x[1], -x[0]))
    print(queue)
