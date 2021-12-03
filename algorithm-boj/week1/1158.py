N, K = [int(x) for x in input().split()]
people = list(range(1, N+1))

idx, result = 0, []
while len(people) != 0:
    idx = (idx + K - 1) % len(people)
    result.append(people.pop(idx))

print('<', end='')
print(*result, sep=', ', end='')
print('>')