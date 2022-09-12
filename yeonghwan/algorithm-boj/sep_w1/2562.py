num_list = []
max_num = 0
order = 0

for i in range(1, 10):
    num_now = int(input())
    if num_now > max_num:
        max_num = num_now
        order = i


print(max_num)
print(order)
