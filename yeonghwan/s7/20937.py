N = map(int, input().split())
dishes = list(map(int, input().split()))

dish_cnt = [0] * 500001

while dishes:
    dish = dishes.pop()
    dish_cnt[dish] += 1

print(max(dish_cnt))