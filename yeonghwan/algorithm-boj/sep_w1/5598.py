encode = input()


decode = ""

for letter in encode:
    decode += chr(ord(letter)-3) if ord(letter) > 67 else chr(ord(letter) + 23)

print(decode)
