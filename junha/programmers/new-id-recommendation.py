def solution(new_id):
    #1
    answer = new_id.lower()

    #2
    answer = ''.join(filter(lambda x: x.islower() or x.isdigit() or x in ['.', '-', '_'], answer))

    #3
    if len(answer) > 0:
        tmp = answer[0]
        for idx in range(1, len(answer)):
            if answer[idx] == '.':
                if answer[idx-1] != '.':
                    tmp += answer[idx]
            else:
                    tmp += answer[idx]
        answer = tmp

    #4
    while len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    while len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    #5, 6
    if len(answer) == 0:
        answer = 'a'
    elif len(answer) >= 16:
        answer = answer[:15]
        while len(answer) > 0 and answer[0] == '.':
            answer = answer[1:]
        while len(answer) > 0 and answer[-1] == '.':
            answer = answer[:-1]
    else:
        pass

    #7
    while len(answer) < 3:
        answer += answer[-1]

    return answer

if __name__ == '__main__':
    print(solution(input()))