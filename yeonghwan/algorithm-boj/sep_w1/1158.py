N, K = map(int, input().split())

circle = [i+1 for i in range(N)]

answer = []

idx = K-1

while len(circle) > 0:

    while idx >= len(circle):
        idx -= len(circle)
    answer.append(circle.pop(idx))
    idx += K-1

answer = [str(i) for i in answer]
print("<" + ', '.join(answer) + ">")
