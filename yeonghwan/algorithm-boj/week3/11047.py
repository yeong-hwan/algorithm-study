N, K = map(int, input().split())

coin_list = [input() for _ in range(N)]
answer = 0

while coin_list:
    coin_now = int(coin_list.pop())
    answer += K // coin_now
    K = K % coin_now


print(answer)
