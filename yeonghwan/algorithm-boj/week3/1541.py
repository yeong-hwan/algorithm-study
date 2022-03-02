from string import digits


line = input().split('-')
ans = 0

for digit in line[0].split('+'):
    ans += int(digit)

eqs = line[1:]
for digits in eqs:
    for digit in digits.split('+'):
        ans -= int(digit)


print(ans)
