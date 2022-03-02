N = int(input())

time_list = list(map(int, input().split()))
time_list.sort()

ans = 0
for i in range(N):
    ans += time_list[i] * (N-i)

print(ans)
