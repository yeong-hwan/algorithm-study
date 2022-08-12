a, b = map(int, input().split())
T = input()
s = ''
decode = []

for letter in T:
    k = ord(letter)-97
    while True:
        n = ((k-b) / a) % 26
        if int(n) == n:
            break
        k += 26
    decode.append(k)

for letter in decode:
    s += chr((int((letter-b) / a) % 26) + 97)

print(s)
