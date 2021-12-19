from sys import stdin, stdout
input = stdin.readline
print = stdout.write

T = int(input())

for _ in range(T):
    binary_num = bin(int(input()))
    for i in range(len(binary_num)-1, 1, -1):
        if int(binary_num[i]) == 1:
            print(f'{len(binary_num) - i -1} ')
