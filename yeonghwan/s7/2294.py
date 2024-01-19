import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins = sorted(list(set(coins)))
# print(coins)

dp = [100001 for _ in range(k+1)]

n = len(coins)

for i in range(n):
    if coins[i] > 10000:
        continue
    if coins[i] >= len(dp):
        continue
    dp[coins[i]] = 1

# print(dp)
for coin in coins:
    for price in range(coin, k+1):
        if price-coin < 0:
            continue
        dp[price] = min(dp[price], dp[price-coin] + 1)

result = dp[k]
if result >= 10001:
    print(-1)
else:
    print(result)
