N = int(input())
dp = [[0] * 10 for _ in range(101)]
dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for degree in range(2, N+1):
    for i in range(10):
        if i == 0:
            dp[degree][i] = dp[degree-1][1]
        elif i == 9:
            dp[degree][i] = dp[degree-1][8]
        else:
            dp[degree][i] = dp[degree-1][i-1] + dp[degree-1][i+1]

print(sum(dp[N]) % 1000000000)
