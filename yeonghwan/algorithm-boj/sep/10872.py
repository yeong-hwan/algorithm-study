N = int(input())

if N != 0:
    ans = N

    while N > 1:
        N -= 1
        ans *= N

    print(ans)
else:
    print(1)
