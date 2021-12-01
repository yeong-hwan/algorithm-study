S = input()
result = [S.find(chr(ord('a') + i)) for i in range(26)]
print(*result, sep=' ')