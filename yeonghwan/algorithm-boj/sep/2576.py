numbers = [int(input()) for _ in range(7)]

odd_list = [number for number in numbers if number % 2 == 1]

if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list))
    print(min(odd_list))
