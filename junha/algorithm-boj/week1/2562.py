maximum, order = 0, 0

for i in range(9):
    x = int(input())
    if x > maximum:
        maximum = x
        order = i+1

print(maximum)
print(order)