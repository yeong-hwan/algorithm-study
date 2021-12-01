from sys import stdin
input = stdin.readline

number_sets = [int(input()) for number in range(9)]
answer = max(number_sets)
print(answer, number_sets.index(answer)+1, sep='\n')
