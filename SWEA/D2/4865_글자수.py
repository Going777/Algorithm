T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    N, M = len(txt), len(pat)
    counts_dict = dict()

    for p in pat:
        counts_dict[p] = 0

    for t in txt:
        if t in counts_dict.keys():
            counts_dict[t] += 1

    max_cnt = 0
    for val in counts_dict.values():
        if max_cnt < val:
            max_cnt = val

    print(f"#{tc} {max_cnt}")