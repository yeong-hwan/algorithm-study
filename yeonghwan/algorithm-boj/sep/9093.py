T = int(input())

for _ in range(T):
    ans = []
    words = list(input().split())
    for word in words:
        ans.append(word[::-1])
    print(" ".join(ans))
