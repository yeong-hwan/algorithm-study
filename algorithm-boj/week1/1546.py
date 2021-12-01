input()
score = [int(x) for x in input().split()]
print(sum(score)/max(score)/len(score)*100)