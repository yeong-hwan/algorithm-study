N = int(input())
price = [0]
m_l = list(map(int, input().split()))
for i in m_l:
    price.append(i)

dp = [0] * 1001
dp[1] = price[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])

print(dp[N])
