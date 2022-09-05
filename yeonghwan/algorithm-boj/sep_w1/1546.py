N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

print(sum(scores) / (M * len(scores)) * 100)
