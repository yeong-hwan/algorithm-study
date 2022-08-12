a, b = map(int, input().split())
N = int(input())
arr = [a, b]

for i in range(N):
    x, y, z = map(int, input().split())
    arr.append(x)
    arr.append(y)
    arr.append(z)
    arr.sort()
    p_1, p_2 = arr[1+i], arr[2*(1+i)+1]
    print(p_1, p_2)
