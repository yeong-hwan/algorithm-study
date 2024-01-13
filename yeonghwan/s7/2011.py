def add(curr, prev):
    number = int(curr + prev)
    # print(number)
    return number


def add_dp(dp, curr, prev):
    dp_now = 0

    if int(prev) > 0:
        dp_now += dp[-1][0]
    if 10 <= add(curr, prev) <= 26:
        dp_now += dp[-2][0]

    dp.append((dp_now % 1000000, curr))


code = list(str(input()).rstrip())

dp = [(1, '-')]
result = None

if code[0] == "0":
    result = 0

for i in range(len(code)):
    curr = code[-1]

    

    if i == 0:
        if curr == "0":
            dp.append((0,curr))
            continue
        dp.append((1, curr))

    else:
        prev = code.pop()        
        curr = code[-1]

        add_dp(dp, curr, prev)


if result == 0:
    print(result)
else:
    # print(dp[-1][0])
    print(dp)