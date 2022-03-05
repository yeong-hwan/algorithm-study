N = int(input())
a, b = 1, 2
for i in range(2, N+1):
    a, b = a+b, a * 3 + b * 2-(a+b)

print((a + b) % 9901)
