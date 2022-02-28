N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * i for i in range(1, N+1)]
dp[0][0] = num[0][0]

for i in range(1, N):
    for j in range(len(num[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + num[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + num[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + num[i][j]

print(max(dp[N-1]))
