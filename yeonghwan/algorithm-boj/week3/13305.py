city = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

ans = 0
cheap = oils[0]

for i in range(len(oils)-1):
    cheap = min(cheap, oils[i])
    ans += cheap * roads[i]

print(ans)
