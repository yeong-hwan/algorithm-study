N = int(input())
K = [input() for _ in range(N)]

T = int(input())
ans = [0] * T
W = [input() for _ in range(T)]

for i in range(len(W)):
    for key in K:
        word = W[i]
        if word == key[:len(word)]:
            ans[i] += 1

for i in ans:
    print(i)
