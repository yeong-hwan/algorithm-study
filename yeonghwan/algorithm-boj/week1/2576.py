from sys import stdin
input = stdin.readline

number_sets = [int(input()) for number in range(7)]
odd_sets = [number for number in number_sets if number % 2 != 0]
if len(odd_sets) == 0:
    print(-1)
else:
    print(sum(odd_sets), min(odd_sets), sep='\n')
