cypher = input()
plain = ''.join([chr((ord(x)-ord('A')-3) % 26 + ord('A')) for x in cypher])
print(plain)