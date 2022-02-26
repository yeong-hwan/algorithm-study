from sys import stdin
input = stdin.readline

N, P = map(int, input().split())
strings = [[] for _ in range(7)]
cnt = 0

for i in range(N):
    string, fret = map(int, input().split())
    string_now = strings[string]

    if len(string_now) == 0:
        cnt += 1
        string_now.append(fret)
    else:
        if string_now[-1] < fret:
            cnt += 1
            string_now.append(fret)
        elif string_now[-1] == fret:
            continue
        else:
            while string_now and string_now[-1] > fret:
                cnt += 1
                string_now.pop()
            if string_now and string_now[-1] == fret:
                continue
            cnt += 1
            string_now.append(fret)

    strings[string] = string_now

print(cnt)
