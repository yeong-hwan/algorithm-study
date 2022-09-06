T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0
    while queue:
        prioritist = max(queue)
        priority_now = queue.pop(0)
        M -= 1

        if prioritist == priority_now:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        
        else:
            queue.append(priority_now)
            if M < 0:
              M = len(queue) - 1