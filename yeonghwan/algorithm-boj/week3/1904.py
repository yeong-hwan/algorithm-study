N = int(input())
dp = [1, 1]

for i in range(2, N+1):
    dp.append((dp[i-1] + dp[i-2]) % 15746)

print(dp[N])
