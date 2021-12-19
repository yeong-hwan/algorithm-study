from sys import stdin
input = stdin.readline

N = int(input())
count = 0
for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            sentence = str(hour) + str(minute) + str(second)
            if '3' in sentence:
                count += 1

print(count)
