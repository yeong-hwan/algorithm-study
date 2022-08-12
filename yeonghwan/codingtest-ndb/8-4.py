N = int(input())

dp = [0, 1]

for i in range(2, N+1):
    dp.append((2 ** i - dp[i-1]) % 796796)

print(dp[N])
