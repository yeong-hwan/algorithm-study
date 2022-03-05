N = int(input())
n_l = list(map(int, input().split()))
M = int(input())
m_l = list(map(int, input().split()))

for m in m_l:
    if m in n_l:
        print(1)
    else:
        print(0)
