N, Q = map(int, input().split())
C = list(map(int, input().split()))
print(N, Q, C)

aval = [[] for _ in range(len(C))]
print(aval)

for i in range(Q):
    order = input()
    if order[0] == 'I':
        k, s = map(int, order[2:].split())
        for j in len(C):
            if len(aval[j]) + s > C[j]:
                continue
            if k in aval[j]:
                aval[j] -=
                aval.remove(k)
                aval[j].append(s)
    elif order[0] == 'F':
        k = int(order[2:])
