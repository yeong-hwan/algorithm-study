import sys
from collections import deque
input = sys.stdin.readline

gear_dict = {}

gear_dict[1] = list(input().rstrip())
gear_dict[2] = list(input().rstrip())
gear_dict[3] = list(input().rstrip())
gear_dict[4] = list(input().rstrip())

# print(gear_dict)

K = int(input())
rotation = deque()

for _ in range(K):
    rotation.append(tuple(map(int, input().split())))


def move_clockwise(gear):
    # 0 -> 1, 1 -> 2, ... , 7 -> 0
    temp = gear.pop()
    gear.insert(0, temp)



def move_counter_clockwise(gear):
    temp = gear.pop(0)
    gear.append(temp)



def get_poles():
    poles = []
    for num, gear in gear_dict.items():
        left, right = gear[-2], gear[2]
        poles.append(left)
        poles.append(right)
        
    return poles


def precise_moving(poles):
    chains = [0, 0, 0]
    # gear1 right == gear2 left
    if poles[1] != poles[2]:
        chains[0] = 1
    if poles[3] != poles[4]:
        chains[1] = 1
    if poles[5] != poles[6]:
        chains[2] = 1

    return chains

def check(idx, chains):
    result = [0, 0, 0, 0]
    # 1
    if idx == 1:
        result[0] = 1
        if chains[0] == 1:
            result[1] = 1
            if chains[1] == 1:
                result[2] = 1
                if chains[2] == 1:
                    result[3] = 1
    # 2
    elif idx == 2:
        result[1] = 1
        if chains[0] == 1:
            result[0] = 1
        if chains[1] == 1:
            result[2] = 1
            if chains[2] == 1:
                result[3] = 1
    # 3
    elif idx == 3:
        result[2] = 1
        if chains[2] == 1:
            result[3] = 1
        if chains[1] == 1:
            result[1] = 1
            if chains[0] == 1:
                result[0] = 1
    # 4
    elif idx == 4:
        result[3] = 1
        if chains[2] == 1:
            result[2] = 1
            if chains[1] == 1:
                result[1] = 1
                if chains[0] == 1:
                    result[0] = 1

    return result

while rotation:
    idx, _wise = rotation.popleft()

    gear = gear_dict[idx]
    
    poles = get_poles()
    chains = precise_moving(poles)

    moving_gears = check(idx, chains)
    # print(chains)
    # print(poles)
    # print(moving_gears)

    for gear_num in range(1, 5):
        if moving_gears[gear_num-1] == 0:
            continue
        
        wise_now = _wise
        # print(gear_num - idx)
        if (gear_num - idx) % 2 != 0:
            wise_now *= -1

        # ccw
        if wise_now == -1:
            move_counter_clockwise(gear_dict[gear_num])
        
        # cw
        elif wise_now == 1:
            move_clockwise(gear_dict[gear_num])

    # print(gear_dict, "\n")

result = 0
multiple = 1

for num, gear in gear_dict.items():
    result += int(gear[0]) * multiple
    multiple *= 2

print(result)