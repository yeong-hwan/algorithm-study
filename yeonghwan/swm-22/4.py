N = int(input())
C = list(map(int, input().split()))
ans = 0

for i in range(len(C)):
    for j in range(i+1, len(C)):
        for k in range(j+1, len(C)):
            if 2000 <= C[i] + C[j] + C[k] <= 2500:
                ans += 1

print(ans)
