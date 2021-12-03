from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
queue = [i for i in range(1, N+1)]
order_number = K-1
answer_queue = []

while len(queue) != 0:
    if order_number+1 <= len(queue):
        answer_queue.append(queue[order_number])
        order_number += K
    # else:
        # order_number %=
