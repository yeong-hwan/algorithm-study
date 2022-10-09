T = int(input())

for _ in range(T):
    N = bin(int(input()))
    N = N[2:]

    answer = []

    for idx in range(len(N)):
        letter = int(N[len(N)-1-idx])

        if letter != 0:
            answer.append(str(idx))

    print(" ".join(answer))
