from sys import stdin, stdout
input = stdin.readline
print = stdout.write

S = input()

for i in range(97, 123):
    if chr(i) in S:
        print(f'{S.index(chr(i))} ')
    else:
        print('-1 ')
