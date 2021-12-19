# from sys import stdin
# input = stdin.readline

T = int(input())

for _ in range(T):
    ps = input()
    balance = 0
    for letter in ps:
        if letter == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            print('NO')
            break
    if balance > 0:
        print('NO')
    elif balance == 0:
        print('YES')
