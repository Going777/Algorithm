T = int(input())
for t in range(1, T+1):
    pat = input()
    txt = input()
    N, M = len(txt), len(pat)
    result = 0
    is_terminate = False
    for i in range(N-M+1):
        for j in range(M):
            if txt[i+j] != pat[j]:
                break
            elif txt[i+j] == pat[j] and j == M-1:
                result = 1
                is_terminate = True
        if is_terminate:
            break
    print(f"#{t} {result}")