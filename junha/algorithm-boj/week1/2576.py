sum, min = 0, 100

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        if n < min:
            min = n
        sum += n

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)