def solution(people, limit):
    answer = 0
    boat_now = 0
    people.sort()

    while len(people) >= 1:
        if len(people) == 0:
            break
        answer += 1
        boat_now += people.pop()
        i = len(people)-1
        print('answer:', answer, 'i:', i, 'people:', people)
        while boat_now < limit:
            print(boat_now, people)
            if i < 0:
                boat_now = 0
                break
            if boat_now + people[i] <= limit:
                boat_now += people.pop(i)
                i -= 1
            else:
                print(i)
                i -= 1

    return answer


print(solution([40, 40, 60, 60, 80, 90], 100))

# 40 40 60 60 80 90
# 100, 4

# 40 40 50 50 60 80 80 80 150
# 240, 3
