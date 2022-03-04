N = int(input())
dp = [[0] * 10 for _ in range(1001)]
dp[1] = [1 for _ in range(10)]
for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N]) % 10007)
