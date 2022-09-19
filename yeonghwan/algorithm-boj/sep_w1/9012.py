T = int(input())

for _ in range(T):
    left, right = 0, 0
    brackets = input()

    pair_point = 0
    flag = False

    for letter in brackets:
        if letter == "(":
            pair_point += 1
        else:
            pair_point -= 1

        if pair_point < 0:
            flag = True
            break

    if pair_point != 0 or flag == True:
        print("NO")
    else:
        print("YES")
