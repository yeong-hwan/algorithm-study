from sys import stdin
input = stdin.readline

N = int(input())
scores = [int(score) for score in input().split()]
M = max(scores)
manipulated_scores = [score/M*100 for score in scores]
avg = sum(manipulated_scores) / N

print(avg)
