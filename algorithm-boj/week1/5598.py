from sys import stdin
input = stdin.readline

before_transition = input()
after_transition = ''

for letter in range(len(before_transition)):
    ascii_num = ord(before_transition[letter])
    if ascii_num > 67:
        after_transition += chr(ascii_num - 3)
    else:
        after_transition += chr(ascii_num + 23)

print(after_transition)
