from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
queue = [i for i in range(1, N+1)]
answer_queue = []
previous_index = K-1

for _ in range(N):
    if previous_index >= len(queue):
        previous_index = previous_index % len(queue)
    answer_queue.append(str(queue.pop(previous_index)))
    previous_index += K-1
print(f'<{", ".join(answer_queue)}>')
