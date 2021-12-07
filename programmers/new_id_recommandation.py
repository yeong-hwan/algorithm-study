def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for word in new_id:
        if word.isalnum() or word in '_-.':
            answer += word
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if len(answer) == 0:
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    print(answer)


solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^."	)
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
