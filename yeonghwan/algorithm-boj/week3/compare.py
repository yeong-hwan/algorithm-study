# 기타의 1~6번줄 각각에 대한 리스트 생성
strings = [[] for _ in range(7)]

res = 0

# 입력받은 음계(줄, 프렛)
for l, f in melody:
    # 해당 줄에 프렛이 하나도 없으면 새로 추가
    if len(strings[l]) == 0:
        strings[l].append(f)
        res += 1

    # 해당 줄에 프렛이 있는 경우
    else:
        # 연주하려는 프렛이 기존의 프렛보다 높은 음이라면, 새로 추가
        if f > strings[l][-1]:
            strings[l].append(f)
            res += 1
            print(strings[l])
        # 연주하려는 프렛이 기존의 프렛과 같은 음이라면, 그냥 지나감
        elif f == strings[l][-1]:
            print(strings[l])
            continue
        # 연주하려는 프렛이 기존의 프렛보다 낮은 음이라면, 연주하려는 프렛보다 높은 음들을 모두 pop
        else:
            while strings[l] and f < strings[l][-1]:
                strings[l].pop()
                res += 1
            if strings[l] and f == strings[l][-1]:
                continue
            # 그리고 나서 연주하려는 프렛 추가
            strings[l].append(f)
            res += 1
print(res)
