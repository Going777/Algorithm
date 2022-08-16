import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T+1):
    txt, pat = input().split()
    N, M = len(txt), len(pat)
    cnt = 0

    i = 0
    while i < N:
        if txt[i:i+M] == pat:
            i += M
        else:
            i += 1
        cnt += 1

    print(f"#{t} {cnt}")