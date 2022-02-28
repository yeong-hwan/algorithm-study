N = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 0, 1

for i in range(2, N+1):
    queue = []
    if i % 3 == 0:
        queue.append(dp[i//3] + 1)
    if i % 2 == 0:
        queue.append(dp[i//2] + 1)
    queue.append(dp[i-1] + 1)
    dp[i] = min(queue)

print(dp[N])
