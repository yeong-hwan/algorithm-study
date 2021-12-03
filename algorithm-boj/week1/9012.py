for _ in range(int(input())):
    flag = True
    count = 0

    for c in input():
        if c == '(':
            count += 1
        else:
            if count == 0:
                flag = False
                break
            count -= 1

    if flag and count == 0:
        print('YES')
    else:
        print('NO')