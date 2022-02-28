N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [0] * N

if N > 2:
    dp[0], dp[1] = wine[0], wine[0] + wine[1]
    dp[2] = max((dp[0] + wine[2]), dp[1], (wine[1] + wine[2]))

    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

    print(dp[-1])
elif N == 1:
    print(wine[0])
else:
    print(wine[0] + wine[1])
