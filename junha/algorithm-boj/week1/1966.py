for _ in range(int(input())):
    N, M = [int(x) for x in input().split()]
    docs = [{"index": idx, "priority": int(x)} for idx, x in enumerate(input().split())]

    for t in range(N):
        target = max(docs, key=lambda x: x["priority"])
        if target["index"] == M:
            print(t+1)
            break

        target_idx = docs.index(target)
        docs = [*docs[target_idx+1:], *docs[:target_idx]]
        